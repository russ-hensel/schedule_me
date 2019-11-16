#!python3
# -*- coding: utf-8 -*-


"""
# Purpose:
#    scheduling app  -- this is the "main program"
#
# Environment ( my dev ):

#        Windows
#        Spyder 3.x
#        Python 3.x
#        Tkinker



"""


import logging
import sys
import os
import time
import datetime
import traceback
import queue
#import threading
import importlib

# ----------- local imports --------------------------
import parameters
import gui
from   app_global import AppGlobal
import schedule_me_helper

# ========================== Begin Class ================================
class ScheduleMe( object ):
    """
    main and controller class for the ScheduleMe application
    """
    def __init__(self ):
        """
        try to get all declared here or restart
        """
        #global print
        # ------------------- basic setup --------------------------------
        print( "" )
        print( "=============== starting ScheduleMe ========================= " )
        print( "" )
        print( "     -----> prints may be sent to log file !" )
        print( "" )

        AppGlobal.controller        = self
        self.app_name               = "ScheduleMe"              # std name often used in other apps
        self.version                = "Ver3 2019 11 09.0"       # std name

        self.gui                    =  None
        self.no_restarts            =  -1

        # ----------- for second thread -------
        self.queue_to_gui           = None
        self.queue_from_gui         = None
#        self.gui_recieve_lock       = threading.Lock()   # when locked the gui will process receive, acquired released in helper
                                                         # how different from just a variable set?
        #self.org_print              = print  # save so can be reset this is the print function
        self.restart( )

    # --------------------------------------------------------
    def restart(self ):
        """
        use to restart the app without ending it
        parameters will be reloaded and the gui rebuilt
        args: zip
        ret: zip ... all sided effects
        """
        print( "===================restart===========================" )
        #global print
        self.no_restarts    += 1
        if self.gui is not None:

            self.logger.info( self.app_name + ": restart" )

            # need to shut down other thread
            self.post_to_queue( "stop", None  , (  ) )
            self.helper_thread.join()

            self.gui.close()
            try:
                importlib.reload( parameters )    # should work on python 3 but sometimes does not
            except Exception as ex_arg:
                reload( parameters )              # this is python 2 but seems to work sometimes

        self.polling_fail         = False   # flag set if polling in gui thread fails

        self.is_first_gui_loop    = True
        self.ext_processing       = None     # built later from parameters if specified
        self.logger               = None     # set later none value protects against call against nothing

        # ----- parameters

        self.parmeters_x          = "none"        # name without .py for parameters extension may be replaced by command line args
        #self.__get_args__( )
        # command line might look like this
        # python smart_terminal.py    parameters=gh_paramaters

        self.parameters         = parameters.Parameters( )  #  std name -- open early may effect other
        self.starting_dir       = os.getcwd()    #

        # get parm extensions  !! will this work on a reload ??
        if self.parmeters_x != "none":
            self.parmeters_xx   =  self.create_class_from_strings( self.parmeters_x, "ParmetersXx" )
            self.parmeters_xx.modify( self.parameters )

        self.logger_id          = self.parameters.logger_id       # std name
        self.logger             = self.config_logger()            # std name

        AppGlobal.logger        = self.logger
        AppGlobal.logger_id     = self.logger_id

        self.prog_info()

        # set up queues before creating helper thread
        self.queue_to_helper    = queue.Queue( self.parameters.queue_length )   # send strings back to tkinker mainloop here
        self.queue_fr_helper    = queue.Queue( self.parameters.queue_length )
        self.helper_thread      = schedule_me_helper.HelperThread( )
        AppGlobal.helper        = self.helper_thread

        self.helper_thread.start()

#        AppGlobal.print_me()        # debug, take out
#        print( "==============================================" )

        self.gui                = gui.GUI(  )
        self.gui.root.after( self.parameters.gt_delta_t, self.polling )
        self.gui.run()

        self.post_to_queue( "stop", None  , (  ) )

        self.helper_thread.join()
        self.logger.info( self.app_name + ": all done" )

    # --------------------------------------------------------
    def config_logger( self, ):
        """
        configure the logger in usual way using the current parameters

        args: zip
        ret:  the logger
        """
        logger = logging.getLogger( self.logger_id  )

        logger.handlers = []
        logger.setLevel( self.parameters.logging_level )     # DEBUG , INFO	WARNING	ERROR	CRITICAL

        fh = logging.FileHandler(   self.parameters.pylogging_fn )
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info( "Done config_logger" ) #  .debug   .info    .warn    .error

        return logger

 # -------------------------------------------------------
    def prog_info( self ):
        """
        log info about program and its argument/environment to the logger
        after logger is set up
        args: zip
        ret:  zip
        log_msg = "a message "
        # debug info warning, error critical
        """
        fll         = AppGlobal.force_log_level
        logger      = self.logger

        if ( self.no_restarts == 0 ) :
            logger.log( fll,  "" )
            logger.log( fll,  "" )
            logger.log( fll,  "============================" )
            logger.log( fll,  "" )

            logger.log( fll,  "Running " + self.app_name + " version = " + self.version ) # + " mode = " + parameters.mode )
            logger.log( fll,  "" )

        else:
            logger.log( fll,  "======" )
            logger.log( fll,  "Restarting " + self.app_name + " version = " + self.version ) #+ " mode = " + parameters.mode )
            logger.log( fll,  "=====" )

        if len( sys.argv ) == 0:
            logger.log( fll, "no command line arg " )
        else:
            ix_arg = 0
            for aArg in  sys.argv:

                logger.log( fll, "command line arg " + str( ix_arg ) + " = " + sys.argv[ix_arg])
                ix_arg += 1

        logger.log( fll,  f"current directory {os.getcwd()}" )
        logger.log( fll,  f"COMPUTERNAME {self.parameters.computername}" )

        start_ts     = time.time()
        dt_obj       = datetime.datetime.utcfromtimestamp( start_ts )
        string_rep   = dt_obj.strftime('%Y-%m-%d %H:%M:%S')
        logger.log( fll, "Time now: " + string_rep )

        return

    # --------------------------------------------------
    def post_to_queue( self, action, function, args ):
        """
        self.post_to_queue( action, function, args )
        """
        loop_flag          = True
        ix_queue_max       = 10
        ix_queue           = 0
        while loop_flag:
            loop_flag      = False
            ix_queue  += 1
            try:
                #print( "try posting " )
                self.queue_to_helper.put_nowait( ( action, function, args ) )
            except queue.Full:

                # try again but give polling a chance to catch up
                print( "smart_terminal queue full looping" )
                self.logger.error( "queue to helper full looping" )
                # protect against infinit loop if queue is not emptied
                if self.ix_queue > ix_queue_max:
                    print( "too much queue looping" )
                    self.logger.error( "too much queue looping" )
                    pass
                else:
                    loop_flag = True
                    time.sleep( self.parameters.queue_sleep )

     # -------------------------------------------------------
    def polling( self, ):
        """
        this is a private method
        polling task runs continually in the GUI
        receiving data is an important task. but is it in this thread  any more  ??
        also auto tasks will be run from here
        polling frequency set via taskDelta, ultimately in parameters
        http://matteolandi.blogspot.com/2012/06/threading-with-tkinter-done-properly.html
        safely invoke the method tk.after_idle to actually schedule the update. That's it!
        """
        """
        queue protocol, data = ( action, function, function_args )
        action            = a string
        function          = a function
        function_args     = arguments to function which will be called  function( function_args ) This should be a tuple
        """
        if self.is_first_gui_loop:
            # if we need a first loop item make a polling_init that is called ??
            # should be moved to gui !! turn back on unless messing up whole app
            # print("lifting...")
#            self.gui.root.attributes("-topmost", True)  # seems to work
#            self.gui.root.lift()                        # did not work
            self.is_first_gui_loop    = False
#            self.gui.root.attributes("-topmost", False)  # seems to work
        try:   # this is for talking with the second thread
            ( action, function, function_args ) = self.rec_from_queue()
            while action != "":
                if action == "call":
                    #print( "controller making call" )
                    sys.stdout.flush()
                    function( *function_args )
                elif action == "rec":
                    self.gui.print_rec_string(  function_args[ 0 ] )
                elif action == "send":
                    # but where is it actually sent ??
                    self.gui.print_send_string( function_args[ 0 ] )
                elif action == "info":
                    self.gui.print_info_string( function_args[ 0 ] )

                ( action, function, function_args ) = self.rec_from_queue()

        except Exception as ex_arg:
            self.logger.error( "polling Exception in smart_terminal: " + str( ex_arg ) )
            # ?? need to look at which we catch maybe just rsh
            (atype, avalue, atraceback)   = sys.exc_info()
            a_join  = "".join( traceback.format_list ( traceback.extract_tb( atraceback ) ) )
            self.logger.error( a_join )

        finally:
            if  self.polling_fail:
                pass
            else:
                #print 'In finally block for cleanup'
                self.gui.root.after( self.parameters.gt_delta_t, self.polling )  # reschedule event

        return

    # --------------------------------------------------
    def rec_from_queue( self, ):
        """
        take an item off the queue, think here for expansion may not be currently used.
        ( action, function, function_args ) = self.rec_from_queue()
        """
        try:
            action, function, function_args   = self.queue_fr_helper.get_nowait()
        except queue.Empty:
            action          = ""
            function        = None
            function_args   = None

        return ( action, function, function_args )

    # ----------------------------------------------
    def os_open_parmfile( self,  ):
        """
        used as callback from gui button
        """
        a_filename = self.starting_dir  + os.path.sep + "parameters.py"
        AppGlobal.os_open_txt_file( a_filename  )

    # ----------------------------------------------
    def os_open_logfile( self,  ):
        """
        used as/by callback from gui button.  Can be called form gt
        """
        AppGlobal.os_open_txt_file( self.parameters.pylogging_fn  )

    # ----------------------------------------------
    def os_open_helpfile( self,  ):
        """
        used as callback from gui button
        """
#        a_filename = self.starting_dir  + os.path.sep + "parameters.py"
        a_filename = self.parameters.help_file
        from subprocess import Popen, PIPE  # since infrequently used
        proc = Popen( [ self.parameters.ex_editor, a_filename ] )

   # ----------------------------------------------
    def cb_gui_test_1( self,  ):
        """
        call back for gui button
        """
        print( "cb_gui_test_1" )

        #----------------------
        ret = AppGlobal.scheduled_event_list.test_query()
        print( ret )
        #self.helper_thread.toggle_lock()

# ========================== Begin Class ================================
class TestAppOne( object ):
    """
    main and controller class for the ScheduleMe application
    """
    def __init__(self ):
        """
        try to get all declared here or restart
        """
        #global print
        # ------------------- basic setup --------------------------------
        print( "" )
        print( "=============== starting TestAppOne ========================= " )
        print( "" )
        print( "     -----> prints may be sent to log file !" )
        print( "" )

        AppGlobal.controller        = self
        self.app_name               = "TestAppOne"              # std name often used in other apps
        self.version                = "Ver2 2018 03 08.02"      # std name

        self.gui                    =  None
        self.no_restarts            =  -1

        # ----------- for second thread -------
        self.queue_to_gui           = None
        self.queue_from_gui         = None
#        self.gui_recieve_lock       = threading.Lock()   # when locked the gui will process receive, acquired released in helper
                                                         # how different from just a variable set?
        #self.org_print              = print  # save so can be reset this is the print function

        self.polling_fail         = False   # flag set if polling in gui thread fails

        self.is_first_gui_loop    = True
        self.ext_processing       = None     # built later from parameters if specified
        self.logger               = None     # set later none value protects against call against nothing

        # ----- parameters

        self.parmeters_x          = "none"        # name without .py for parameters extension may be replaced by command line args
        #self.__get_args__( )
        # command line might look like this
        # python smart_terminal.py    parameters=gh_paramaters

        self.parameters         = parameters.Parameters( )  #  std name -- open early may effect other
        self.starting_dir       = os.getcwd()    #

        # get parm extensions  !! will this work on a reload ??
        if self.parmeters_x != "none":
            self.parmeters_xx   =  self.create_class_from_strings( self.parmeters_x, "ParmetersXx" )
            self.parmeters_xx.modify( self.parameters )

        self.logger_id          = self.parameters.logger_id       # std name
        self.logger             = self.config_logger()            # std name

        AppGlobal.logger        = self.logger
        AppGlobal.logger_id     = self.logger_id

        # self.prog_info()

#        # set up queues befor creating helper thread
#        self.queue_to_helper    = queue.Queue( self.parameters.queue_length )   # send strings back to tkinker mainloop here
#        self.queue_fr_helper    = queue.Queue( self.parameters.queue_length )
#        self.helper_thread      = schedule_me_helper.HelperThread( )
#        AppGlobal.helper        = self.helper_thread
#
#        self.helper_thread.start()
#
##        AppGlobal.print_me()        # debug, take out
##        print( "==============================================" )
#
#        self.gui                = gui.GUI(  )
#        self.gui.root.after( self.parameters.gt_delta_t, self.polling )
#        self.gui.run()
#
#        self.post_to_queue( "stop", None  , (  ) )
#
#        self.helper_thread.join()

#        # ============== test here ===========
#        import db
#        a_db            = db.DBAccess()
#        a_dict_name     = "greenhouse"
#        db_connect_ok   = a_db.open( a_dict_name )
#        msg             = "ok"
#
#        fetched_data    = []
#
#        if  not( db_connect_ok):
#            msg    = "no_db_connect"
#            #return msg
#        else:
#            msg    = "connect_good"
#        print( msg)

        msg = self.app_name + ": all done"
        print( msg )
        self.logger.info( self.app_name + ": all done" )

    # --------------------------------------------------------
    def config_logger( self, ):
        """
        configure the logger in usual way using the current parameters

        args: zip
        ret:  the logger
        """
        logger = logging.getLogger( self.logger_id  )

        logger.handlers = []
        logger.setLevel( self.parameters.logging_level )     # DEBUG , INFO	WARNING	ERROR	CRITICAL

        fh = logging.FileHandler(   self.parameters.pylogging_fn )
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info( "Done config_logger" ) #  .debug   .info    .warn    .error

        return logger

# ==============================================
if __name__ == '__main__':
    """
    run the app here for convenience of launching
    """
    a_app = ScheduleMe(  )


#    a_app = TestAppOne(  )





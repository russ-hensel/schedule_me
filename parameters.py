# -*- coding: utf-8 -*-

# parameters    for ScheduleMe

# History/status
#    ** from the smart terminal

import logging
#import serial
import sys
import datetime
import os

#--------local
import schedule_me
import schedule_me_helper
from   app_global import AppGlobal

class Parameters( object ):
    """
    sets parameter values, globally available thru AppGlobal
    """
    def __init__(self,  ):
        self.controller       = AppGlobal.controller
        AppGlobal.parameters  = self

        self.default_parms()
        self.os_tweaks()
        self.computer_name_tweaks()
        #self.mode_1()
        self.mode_2()
        self.init_function_2    = None

    # -------
    def os_tweaks( self ):
        """
        this is an subroutine to tweak the default settings of "default_terminal_mode"
        for particular operating systems
        """
        if  self.os_win:
            self.icon              = r"./green_house.ico"    #  greenhouse this has issues on rasPi
            #self.icon              = None                   #  default gui icon

        else:
            pass

    # -------
    def computer_name_tweaks( self ):
        """
        this is an subroutine to tweak the default settings of "default_terminal_mode"
        for particular computers.  Put in settings for you computer if you wish
        """

        if self.computername == "smithers":
            self.port               = "COM5"   #
            #self.port              = "COM3"   #
            self.win_geometry       = '1450x700+20+20'      # width x height position
            self.ex_editor          =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10 smithers

        elif self.computername == "millhouse":
            pass
            self.port               = "COM3"   #
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"    # russ win 10 millhouse
            #self.win_geometry   = '1300x600+20+20'          # width x height position

    # -------
    def mode_2(self,  ):

        self.mode     = "Mode 2"

        #--------------- appearance ---------
#        self.win_geometry      = '1300x700+20+20'    # width x height position
#
#        self.id_color          = "red"    #  "blue"   "green"  and lots of other work
#        self.id_height         = 20       # height of id pane, 0 for no pane
#        self.id_color          = "green"
#        self.bk_color          = "blue"   # color for the background, you can match the id color or use a neutral color like gray
#        self.bk_color          = "gray"   #

        self.logging_level     = logging.DEBUG           #   CRITICAL	50   ERROR	40 WARNING	30  INFO	20 DEBUG	10 NOTSET	0

        # -----  external exe and files  ----------------
#        self.ex_editor   =  r"leafpad"    # linux maybe
#        if self.our_os == "win32":
#            self.ex_editor   =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10
#
#        self.help_file       =  r"schedule_me_help.txt"

        #------------------- email
        self.email_to_address   = "russ_hensel@comcast.net"
        self.email_server       = "smtp.gmail.com"
        self.email_port         = 587

        self.email_from_address = "russ.hensel@gmail.com"
        self.email_account      = "russ.hensel@gmail.com"

        self.email_account_pass = "tentothe100!"

        self.email_min_repeat_time  = datetime.timedelta( days= 1, hours = 0, minutes = 1  )
        self.email_max_count    = 3

        # ----------------------- data

        #toaddr          = "squeakathighrant@gmail.com"

        #----------------- db connect in subroutines -- subroutines make it easire to switch sets of parameters

        #  self.select_timedelat  = datetime.timedelta( days= 0, hours = 0, minutes = 30  )
        # self.dbRtoPi181( ")     # 181 is root cellar enviromental monitor

        self.create_parm_dict_greenhouse( )
        self.create_parm_dict_rootcellar( )
        self.create_parm_dict_rootcellar_191( )

        return

      # -------
    def mode_1(self,  ):

        self.mode     = "Mode 1"

        #--------------- appearance ---------
        self.win_geometry      = '1300x700+20+20'    # width x height position

        self.id_color          = "red"    #  "blue"   "green"  and lots of other work
        self.id_height         = 20       # height of id pane, 0 for no pane
        self.id_color          = "green"
        self.bk_color          = "blue"   # color for the background, you can match the id color or use a neutral color like gray
        self.bk_color          = "gray"   #

        # -----  external exe and files  ----------------
        self.ex_editor   =  r"leafpad"    # linux maybe
        if self.our_os == "win32":
            self.ex_editor   =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10

        self.help_file       =  r"schedule_me_help.txt"

        #------------------- email
        self.email_to_address   = "russ_hensel@comcast.net"
        self.email_server       = "smtp.gmail.com"
        self.email_port         = 587

        self.email_from_address = "russ.hensel@gmail.com"
        self.email_account      = "russ.hensel@gmail.com"

        self.email_account_pass = "tentothe100!"

        self.email_min_repeat_time  = datetime.timedelta( days= 1, hours = 0, minutes = 1  )
        self.email_max_count    = 3

        # ----------------------- data

        self.alarm_min_temp     = 50        # farenheight
        self.alarm_max_temp     = 75

        #toaddr          = "squeakathighrant@gmail.com"

        #----------------- db connect in subroutines -- subroutines make it easire to switch sets of parameters

        #self.select_timedelat  = datetime.timedelta( days= 0, hours = 0, minutes = 30  )
        #self.dbRtoPi181( ")     # 181 is root cellar enviromental monitor

        return

    # -------
    def default_parms(self,  ):
        self.mode               = "Default"
        #--------------- automatic -----------------
        self.our_os = sys.platform       #testing if our_os == "linux" or our_os == "linux2"  "darwin"  "win32"
        # print( "our_os is ", our_os )

        if self.our_os == "win32":
            self.os_win = True     # right now windows and everything like it
        else:
            self.os_win = False

        self.platform           = self.our_os    # sometimes it matters which os
        self.opening_dir        = os.getcwd()
        self.computername       = os.getenv( "COMPUTERNAME" ) # what in linux

        #--------------- for mode ---------

        self.mode               = "Default"
        self.init_function_2    = None
        #--------------- appearance ---------
        self.win_geometry      = '1300x700+20+20'    # width x height position

        self.id_color          = "red"    #  "blue"   "green"  and lots of other work
        self.id_height         = 20       # height of id pane, 0 for no pane
        self.id_color          = "green"
        self.bk_color          = "blue"   # color for the background, you can match the id color or use a neutral color like gray
        self.bk_color          = "gray"   #

         # ----- logging ------------------
        # id used by the python logger  -- appears inside the logging file
        self.logger_id         = "sch_me"
        self.pylogging_fn      = "schedule_me.py_log"   # file name for the python logging
        self.logging_level     = logging.DEBUG           #   CRITICAL	50   ERROR	40 WARNING	30  INFO	20 DEBUG	10 NOTSET	0
        #self.logging_level     = logging.INFO            #   CRITICAL	50   ERROR	40 WARNING	30  INFO	20 DEBUG	10 NOTSET	0
        self.print_to_log       = False

        # ----- message area in gui   -----------
        self.default_scroll     = 1        # 1 auto scroll the recieve area, else 0
        self.max_lines          = 1000

        self.gt_delta_t         = 100              # in ms --   lowest I have tried is 10 ms, could not see cpu load

        self.ht_delta_t         = 10000/1000.      # this uses time so in seconds, convert to ms sorry for confusion

        self.queue_sleep         = .1
        self.queue_length        = 20

        self.prefix_info        = "# !!! "    # prefix for informational messages

        # -----  external exe and files  ----------------
        self.ex_editor   =  r"leafpad"    # linux maybe
        if self.our_os == "win32":
            self.ex_editor   =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10

        self.help_file       =  r"schedule_me_help.txt"

        #------------------- email
        self.email_to_address   = "russ_hensel@comcast.net"
        self.email_server       = "smtp.gmail.com"
        self.email_port         = 587

        self.email_from_address = "russ.hensel@gmail.com"
        self.email_account      = "russ.hensel@gmail.com"

        self.email_account_pass = "tentothe100!"

        self.email_min_repeat_time  = datetime.timedelta( days= 1, hours = 0, minutes = 1  )
        self.email_max_count    = 3

        # ----------------------- data

        self.alarm_min_temp     = 50        # farenheight
        self.alarm_max_temp     = 75

        #toaddr          = "squeakathighrant@gmail.com"

        #----------------- db connect in subroutines -- subroutines make it easire to switch sets of parameters

        #self.select_timedelat  = datetime.timedelta( days= 0, hours = 0, minutes = 30  )
        #self.dbRtoPi181()

        return

    # ------------------------ make this select base on mode ------------
    def init_from_helper( self ):
         #def build_future_events( self ):
         """
         call after helper is built -- look at: ScheduleMeHelper.run() may move to restart??
         build the event here
         put in parameters, controller....... AppGlobal
         see event_list.run_event() to see how the functions are run
         """
         event_list                         = schedule_me_helper.ScheduledEventList( )
         AppGlobal.scheduled_event_list     = event_list

         # seems to be a problem about when the functions are evaluated, need helper to be define
         # so event.list.fe_post_message can be evaluated ??

         dt_soon        = ( datetime.datetime.now() +
                                    datetime.timedelta( minutes = 1  ) )

         #time_tuple     = time.localtime( dt_now )
         time_tuple     = dt_soon.timetuple()
         soon_hr        = time_tuple[3]          # used to schedule close to startup  see time delat above
         soon_min       = time_tuple[4]

         #------------ the events begin here

         self.add_event_next_given_time(    a_name = "test fe_db_fetch_email for greenhouse",
                                            a_minute                = soon_min,
                                            a_hour                  = soon_hr,
                                            a_day                   = None,       # default to today
                                            a_parameter_dict_name   = "greenhouse",
                                            #a_timedelta             = datetime.timedelta( days   = 1 ),
                                            a_timedelta             = datetime.timedelta( minutes = 10 ), # seconds
                                            #a_timedelta             = datetime.timedelta( seconds = 50 ), # seconds
                                            a_count                 = -1,
                                            a_function              = event_list.ef_db_fetch_email,
                                            a_reschedule_function   = event_list.erf_reschedule_deltat_t   )  # run_reschedule_deltat_t function in helper



         # self.add_event_next_given_time(    a_name = "test fe_db_fetch_email for rootcellar",
                                            # a_minute                = soon_min,
                                            # a_hour                  = soon_hr,
                                            # a_day                   = None,       # default to today
                                            # a_parameter_dict_name   = "rootcellar",
                                            # #a_timedelta             = datetime.timedelta( days   = 1 ),
                                            # a_timedelta             = datetime.timedelta( minutes = 14 ), # days, minutes, seconds
                                            # #a_timedelta             = datetime.timedelta( seconds = 60 ), # seconds
                                            # a_count                 = -1,
                                            # a_function              = event_list.ef_db_fetch_email,
                                            # a_reschedule_function   = event_list.erf_reschedule_deltat_t   )  # run_reschedule_deltat_t function in helper


         self.add_event_next_given_time(    a_name = "test fe_db_fetch_email for new rootcellar piz_1_191",
                                            a_minute                = soon_min,
                                            a_hour                  = soon_hr,
                                            a_day                   = None,       # default to today
                                            a_parameter_dict_name   = "rootcellar_191",
                                            #a_timedelta             = datetime.timedelta( days   = 1 ),
                                            a_timedelta             = datetime.timedelta( minutes = 17 ), # days, minutes, seconds
                                            #a_timedelta             = datetime.timedelta( seconds = 60 ), # seconds
                                            a_count                 = -1,
                                            a_function              = event_list.ef_db_fetch_email,
                                            a_reschedule_function   = event_list.erf_reschedule_deltat_t   )  # run_reschedule_deltat_t function in helper

#         self.add_event_next_given_time(    a_name = "event 2",
#                                            a_minute = soon_min, a_hour = soon_hr, a_day = None,
#                                            #a_timedelta             = datetime.timedelta( days   = 1 ),
#                                            #a_timedelta             = datetime.timedelta( minutes = 1 ), # seconds
#                                            a_timedelta             = datetime.timedelta( seconds = 70 ), # seconds
#                                            a_count                 = 3,
#                                            a_function              = event_list.fe_post_message,
#                                            a_reschedule_function   = event_list.run_reschedule_deltat_t   )
#
#         self.add_event_next_given_time(    a_name = "event 3",
#                                            a_minute = soon_min, a_hour = soon_hr, a_day = None,
#                                            #a_timedelta             = datetime.timedelta( days   = 1 ),
#                                            #a_timedelta             = datetime.timedelta( minutes = 1 ), # seconds
#                                            a_timedelta             = datetime.timedelta( seconds = 200 ), # seconds
#                                            a_count                 = -1,
#                                            a_function              = event_list.fe_post_message,
#                                            a_reschedule_function   = event_list.run_reschedule_deltat_t   )
#
    def old_init( self ):

        # =========== meta parms, set other parms ===========
        # these parameters are used to set other parameters as a convenience, if this is not convienuent for you just
        # set your parmeters at the end of the init or us a second parameter file.
    # ------->> Meta, parameters that may be used for convienence to change the value of other parameters

        # -----  mode ... ----------------
        # mode might be called application it changes the function of the
        # app, mostly in the "auto" mode, it primarly effects the auto task list
        # and perhaps the database connection

        # this is the name of a connection
        self.connect     = "none"        # default - do not even try to connect

        self.print_to_log      = False
        # ----- send/recieve/recieve area and presets  -----------

        self.show_helper_frame   = False       # helper frame may be just for debugging ??

        # ------ presets for send areas, lots of stuff once used now commented out, may branch on mode in future
        # for MPMotor

        #   could be just string or tuples, this will try tuple   (  label, data_to_send, enable_fg )  ( "Send", "send_me", true )  or mixed, test type on each
        #  "\n"    for a 2 line label on the button


#        # probably being phased out or not but do not use
#        self.loop_period       = 100              # multiples of self.poll_delta_t
#        self.loop_text         = "looping TEXT"   # do not make so long as to jam the transmitter sent every poll_delta_t

        # This is how often in ms to poll the comm port, faster makes it more responsive, uses
        # more resources
        self.gt_delta_t        = 100              # in ms --   lowest I have tried is 10 ms, could not see cpu load

        self.ht_delta_t        = 100/1000.        # this uses time so in seconds, convert to ms sorry for confusion

        self.send_array_mod    = 5                # see task, send array

        # ?? not implemented should it be?

        self.win_geometry      = '1300x700+20+20'    # width x height position
        if our_os == "win32":
            self.win_geometry      = '1500x800+20+20'    # width x height position

        # sets a color that you like or so that differently configured
        # smart terminal are easily distinguished
        self.id_color          = "red"    #  "blue"   "green"  and lots of other work
        self.id_height         = 20       # height of id pane, 0 for no pane
        self.id_color          = "green"
        self.bk_color          = "blue"   # color for the background, you can match the id color or use a neutral color like gray
        self.bk_color          = "gray"   #

        # specify an icon for the application window
        #  this may be an issue for linux, have some code to skip icon there, need to find out more
        self.icon              = r"D:\Temp\ico_from_windows\terminal_red.ico"    #  blue red green yellow
        self.icon              = r".smaller.ico"    #  this format is ng
        self.icon              = r"D:\Russ\0000\SpyderP\SmartTerminal\smaller.ico"    #  greenhouse will rename
        self.icon              = r"smaller.ico"    #  greenhouse will rename  == this has issues on rasPi
        self.icon              = r"./smaller.ico"    #  greenhouse will rename  == this has issues on rasPi

        self.ex_editor        =  r"leafpad"    # linux maybe
        if our_os == "win32":
            self.ex_editor   =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10

        self.help_file       =  r"schedule_me_help.txt"
        #self.grapher         =  r"D:\Russ\0000\SpyderP\smart_terminal_graph\smart_terminal_graph.py"

    # ------->> Communications
        # -----  parameters that are relavant for rs232 parms for arduino

        # ----- Processing Monitor application Values use may depend on mode  ===============

        self.ex_max              = 5   # max no of exceptions for some reason
        # ----- data valid and db update rules -------------------


        # print "Parameters initialized"
        # too soon to use logger, not configured yet
        # self.controller.logger.info( "parameters.Parameters initialized" )
        return

    # ------->> Parameter dicts   -- set up not tested

    #   ------------------------------------
    def create_parm_dict_greenhouse( self, ):
        """
        parameters for the greenhouse event(s)
        """
        dict_name                       = "greenhouse"       # name for this in the dict of dictionaries
        a_dict                          = {}                 # empty dict

        a_dict["db_host"]               = '192.168.0.189'    # add the tcpip address of database server
        a_dict["db_port"]               = 3306               # database server port -- here default for mysql
        a_dict["db_db"]                 = 'pi_db'            # name of the database/schema

        a_dict["db_user"]               = 'pi_user'          # name of the database user
        a_dict["db_passwd"]             = 'taunot3point1fourpi'      # password for this user at this tcpip address

        # next the sql used to select from the database table
        a_dict["sql_select"]            = "SELECT ev_time, temp_1, humid_1 FROM ev_data           WHERE ( ev_time > %s ) order by temp_1 asc"


        a_dict["select_timedelat"]      = datetime.timedelta( days= 0, hours = 0, minutes = 30  ) # time used in the database select

        a_dict["alarm_min_temp"]        = 50        # ( farenheight ) used to set allarm ( email ) if temp gets too low
        a_dict["alarm_max_temp"]        = 75        # ( farenheight ) used to set allarm ( email ) if temp gets too high

        a_dict["failed_connect_count"]  = 0         # used as variable to count how many db connects in a row fail
        a_dict["max_connect_count"]     = 4         # at this number of faild connects an email is trigged
        a_dict["min_repeat_email_time"] = datetime.timedelta( days= 1, hours = 0, minutes = 0  )   # no emails repeated for this time period
        a_dict["time_last_email"]       = None      # time last email was sent

        AppGlobal.parameter_dicts[dict_name] = a_dict   # put in the AppGlobal dictionary

    #   ------------------------------------
    def create_parm_dict_rootcellar( self, ):
            """
            pairs with some init_from_helper parms
            """
            dict_name                     = "rootcellar"
            a_dict                        = {}

            a_dict["db_host"]             = '192.168.0.181'   #
            a_dict["db_port"]             = 3306
            a_dict["db_db"]               = 'env_data_1'

            a_dict["db_user"]             = 'env_user'
            a_dict["db_passwd"]           = 'pi_not_tau'

            a_dict["sql_select"]          = "SELECT gh_time, temp_1, humid_1 FROM env_data_table_1  WHERE ( gh_time > %s ) order by temp_1 asc"
            a_dict["select_timedelat"]    = datetime.timedelta( days= 0, hours = 0, minutes = 30  )

            a_dict["alarm_min_temp"]      = 50        # farenheight
            a_dict["alarm_max_temp"]      = 75

            a_dict["failed_connect_count"]  = 0
            a_dict["max_connect_count"]     = 4           # at 4 trigges an email
            a_dict["min_repeat_email_time"] = datetime.timedelta( days= 1, hours = 0, minutes = 0  )
            a_dict["time_last_email"]       = None

            AppGlobal.parameter_dicts[dict_name] = a_dict

    #   ------------------------------------
    def create_parm_dict_rootcellar_191( self, ):
            """
            pairs with some init_from_helper parms
            """
            dict_name                     = "rootcellar_191"
            a_dict                        = {}

            a_dict["db_host"]             = '192.168.0.191'   #
            a_dict["db_port"]             = 3306
            a_dict["db_db"]               = 'pi_db'

            a_dict["db_user"]             = 'pi'
            a_dict["db_passwd"]           = 'KirscheTauEpoint14'

            a_dict["sql_select"]          = "SELECT env_timestamp, temp_1, humid_1 FROM env   WHERE ( env_timestamp > %s ) order by temp_1 asc"
            a_dict["select_timedelat"]    = datetime.timedelta( days= 0, hours = 0, minutes = 30  )

            a_dict["alarm_min_temp"]      = 38        # farenheight
            a_dict["alarm_max_temp"]      = 65

            a_dict["failed_connect_count"]  = 0
            a_dict["max_connect_count"]     = 4           # at 4 trigges an email
            a_dict["min_repeat_email_time"] = datetime.timedelta( days= 1, hours = 0, minutes = 0  )
            a_dict["time_last_email"]       = None

            AppGlobal.parameter_dicts[dict_name] = a_dict


    # ------->> Subroutines:  db set connection parameter
    #  these will probably not apply to your setup

    # ----- db remote generic, still needs host from a caller # make add to passed dict ??
    def dbRemote( self, ):
        """
        standard parameters for remote connection, but
        will not set host which needs to be set in caller
        return: set of instance variables
        """
        self.db_host             = '192.168.0.0'   # no pi of mine
        self.db_host             = 'host not set'  # no pi of mine
        self.db_port             = 3306

        self.db_db               = 'env_data_1'

        self.db_user             = 'env_user'
        self.db_passwd           = 'pi_not_tau'

    # ----- db on standard local name, move towards workin on all my pi's
    def dbLocal( self, ):

        self.db_host             = '127.0.0.1'
        self.db_port             = 3306

        self.db_db               = 'env_data_1'

        self.db_user             = 'env_user'
        self.db_passwd           = 'pi_not_tau'

    # ----------------------- db on .....  ----------------------
    def dbRtoPi181( self, ):   # make add to passed dict ?

        self.db_host             = '192.168.0.181'
        self.db_port             = 3306

        self.db_db               = 'env_data_1'

        self.db_user             = 'env_user'
        self.db_passwd           = 'pi_not_tau'

    #   ------------------------------------

     # ----- db remote to a Pi  189

    def dbRtoPi189( self, ):

        self.dbRemote( )
        self.connect             = "RtoPi189"
        self.db_host             = '192.168.0.189'    # 178 even ethernet, 179 odd wifi
        self.db_db               = 'pi_db'

        self.db_user             = 'pi_user'
        self.db_passwd           = 'taunot3point1fourpi'


    # -------------------------------
    def add_event_next_given_time( self, a_name,
                                  a_parameter_dict_name,          # this may take over all others
                                  a_minute = 0, a_hour = 0, a_day = None,
                                  a_timedelta               = None,
                                  a_count                   = 1,
                                  a_function                = None,
                                  a_reschedule_function     = None,   ):

        """
        !! really need to explain here
        """

        event_time     = dt_next_given_time( a_minute = a_minute, a_hour = a_hour, a_day = a_day )

        a_event = schedule_me_helper.ScheduledEvent( event_name = a_name,
                                         a_parameter_dict_name  = a_parameter_dict_name,          # this may take over all others
                                         event_function         = a_function,
                                         event_time             = event_time,
                                         reschedule_function    = a_reschedule_function,
                                         rs_1                   = a_count,
                                         rs_2                   = a_timedelta )

        event_list      = AppGlobal.scheduled_event_list
        event_list.add_event( a_event )

    #   ------------------------------------
    def __set_default__xxxx(self, ):
        """
        this sets defaults that are needed to make the system run, many have an advanced
        purpose and will not be documented ( comments here should not be trusted )
        here, other example parameter files document
        them, unless they are obsolete or unimplemented.  Setting unused parameters
        just wastes small amounts of memory, impact is minimal
        """


        #---------------- end meta parameters --------------------
        self.queue_length         = 20
        self.queue_sleep          = .1

        # automatically start the task list
        #self.task_list_on         = False   no longer exists


        # ----- send/recieve/recieve area and presets  -----------
        self.kivy                 = False
        self.max_lines            = 1000     # max number of lines in the recieve area
        # number of lines in the recieve area before older lines are truncated
        # limits memory used  0 for unlimited

        # determine if the receive auto scrolls or not -- also a check box in the gui
        self.default_scroll    = 1        # 1 auto scroll the recieve area, else 0

        #import  gh_processing
        # ----------  self.start_helper_function    = gh_processing.GHProcessing.find_and_monitor_arduino
        self.start_helper_function    = "find_and_monitor_arduino"    # now using eval, may need to do same with args,
        self.start_helper_args        = ( )     # () empty   ( "x", ) one element
        self.start_helper_delay       = 0      # in seconds  must be > 0 to start

        # open comm port on startup
        self.auto_open         = False       # true to open port on start up  #  !! *todo

        # number of send frames in the gui
        self.gui_sends         = 5         # number of send frames in the gui beware if 0
        self.max_send_rows     = 1         # the send areas are added in columns this many rows long, then a new

        self.show_helper_frame = False      # helper frame not used in basic terminal

        # ------ pre-sets for send areas

        #   could be just string or tuples, this will try tuple   (  label, data_to_send, enable_fg )  ( "Send", "send_me", true )  or mixed, test type on each
        #  "\n"    for a 2 line label on the button


        # This is how often in ms to poll the comm port, faster makes it more responsive, uses
        # more resources
        self.gt_delta_t        = 100              # in ms --   lowest I have tried is 10 ms, could not see cpu load

        self.ht_delta_t        = 100/1000.        # this uses time so in seconds, sorry for confusion

        self.send_array_mod    = 5                # see task, send array

        # ?? not implemented should it be?
        self.block_port_closed = False            # block sending if port is closed   # *todo  -- or some warning

        # ----- appearance: size, color, icon.... ------------------------
        # sets the initial overall window size - it is an oddly formatted string
        # self.win.geometry('1500x800+40+80')




        # specify an icon for the application window
        #  this may be an issue for linux, have some code to skip icon there, need to find out more
        self.icon              = r"D:\Temp\ico_from_windows\terminal_red.ico"    #  blue red green yellow
        self.icon              = r".smaller.ico"    #  this format is ng
        self.icon              = r"D:\Russ\0000\SpyderP\SmartTerminal\smaller.ico"    #  greenhouse will rename
        self.icon              = r"smaller.ico"    #  greenhouse will rename  == this has issues on rasPi
        self.icon              = r"./smaller.ico"    #  greenhouse will rename  == this has issues on rasPi
        self.icon              = None

    # ------->> Communications
        # -----  parameters that are relavant for rs232 parms for arduino

        # 9600 is ok as are many others try this for most reliable? comm
        # The default is 8 data bits, no parity, one stop bit.
        # http://arduino.cc/en/Serial/begin
        # ----- ports and  serial settings -------------------------
        # wrappers for PySerial, leave alone unless more drivers are implemented
     # used to probe around for ports

        # ----- Processing Monitor application Values use may depend on mode  ===============

        self.ex_max              = 20   # max no of exceptions for some reason

        # next are caused by too many or wrong kinds of exceptions.
        self.after_helper_fail  = "do something"
        self.after_polling_fail      = "do something and more parameters "

# ----------------------------
def dt_next_given_time( a_minute = 0, a_hour = 0, a_day = None ):
    """
    returns datetime ( dt ) with a given hour ( 24 hr clock, and minute, and oprionally day ( beware too high )
    today or tomorrow if in the past
    """
    dt_now     = datetime.datetime.now()
    dt_trial   = dt_now.replace( hour = a_hour, minute = a_minute, second = 0, microsecond = 0 )
    if a_day is not None:
        dt_trial = dt_trial.replace( day = a_day )

    if dt_now > dt_trial :
        dt_final   = dt_trial + datetime.timedelta( days = 1 )  # can have multiple args.....
    else:
        dt_final   = dt_trial

    return dt_final

# ----------------------------

# ==============================================
if __name__ == '__main__':
    """
    run the app here for convenience of launching
    """
    print( "" )
    print( " ========== starting ScheduleMe from parameters.py ==============" )
    import schedule_me
    a_app = schedule_me.ScheduleMe(  )


# =================== eof ==============================











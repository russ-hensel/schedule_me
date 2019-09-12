# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 21:06:50 2017

@author: Russ
"""
#typical use
#from app_global import AppGlobal
#
#self.parameters    = AppGlobal.parameters

import sys


class AppGlobal( object ):
    """
    manages parameter values for all of Smart Terminal app and its various data logging
    and monitoring applications
    generally available to most of the application through the Controllers instance variable
    """
    force_log_level         = 99    # value to force logging, high but not for errors

    controller              = None
    parameters              = None
    logger                  = None
    logger_id               = None
    scheduled_event_list    = "None"
    helper                  = "None"
    parameter_dicts         = {}         # set up in parameters ????? -- see and example std setup somw where

    def __init__(self,  controller  ):

        #self.__mandatory__( controller )  # should always be used, never ( almost? ) modified
        #self.__set_default__()            # this is not required in general but lets you ignore the setting of more advanced parameters
        pass

#        controller     = None
#        parameters     = None
#        logger         = None
 #
#        self.logger             = logging.getLogger( self.controller.logger_id + ".gui")
#        #self.logger.info( "in class gui.GUI init")


    # ----------------- debuging ----------------
    def to_str():
        """
        convert some of AppGlobals contents to a string for debugging
        """
         a_string   = (   "AppGlobal" +
                                  str (AppGlobal.parameter_dicts ) +
                           "\n    ---------- greenhouse ----------\n" + str( AppGlobal.parameter_dicts["greenhouse"]) +
                           "\n    ---------- rootcellar ----------\n" + str( AppGlobal.parameter_dicts["rootcellar"])     )
         return a_string

    def print_me():
         sys.stdout.flush()
         print("========== AppGlobal =================")
         print( AppGlobal.to_str( ) )
         sys.stdout.flush()



# ==============================================
if __name__ == '__main__':
    """
    run the app here for convenience of launching
    """
    print( "" )
    print( " ========== starting ScheduleMe from sch_me.py ==============" )
    import schedule_me
    a_app = schedule_me.ScheduleMe(  )



# ======================== eof ======================
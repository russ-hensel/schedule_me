D:\Russ\0000\FreeCad\arduinoNano

run tasks on some sort of schedule
email if get bad results

--------------------



------------------ copied from ui, find corresponding log   --------------------

# !!! 2018-03-08 08:27:06.614834 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! 2018-03-08 08:33:06.640139 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 08:41:06.679493 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! 2018-03-08 08:43:06.724142 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 08:53:06.766201 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! At time: 2018-03-08 08:53:06.788655 in event test fe_db_fetch_email for greenhouse
 we got a 'bad' return = no_db_connect
# !!! 2018-03-08 08:55:06.800001 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! 2018-03-08 09:03:06.837381 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 09:09:06.886385 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! At time: 2018-03-08 09:09:06.891207 in event test fe_db_fetch_email for rootcellar
 we got a 'bad' return = no_db_connect
# !!! 2018-03-08 09:13:06.908936 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 09:23:06.951627 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 09:23:16.989329 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! 2018-03-08 09:33:07.030838 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 09:37:07.090442 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! 2018-03-08 09:43:07.117402 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 09:51:07.162136 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! 2018-03-08 09:53:07.177611 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 10:03:07.219662 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
# !!! 2018-03-08 10:05:07.259486 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
# !!! 2018-03-08 10:13:07.297395 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse


----- and the log  --------
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:27:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 08:27:06,614 - sch_me - DEBUG - 2018-03-08 08:27:06.614834 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 08:27:06,615 - sch_me - INFO - in class DBAccess init
2018-03-08 08:27:06,615 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 08:27:06,615 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 08:27:06,616 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 08:27:06,616 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 08:27:06,616 - sch_me - DEBUG - 3306
2018-03-08 08:27:06,617 - sch_me - ERROR - a_dict["failed_connect_count = "]2
2018-03-08 08:27:06,617 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 08:27:06,618 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:41:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 08:27:06,618 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 08:27:06,619 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:41:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 08:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 08:33:06,640 - sch_me - DEBUG - 2018-03-08 08:33:06.640139 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 08:33:06,641 - sch_me - INFO - in class DBAccess init
2018-03-08 08:33:06,641 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 08:33:06,642 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 08:33:06,642 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 08:33:06,642 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 08:33:06,643 - sch_me - DEBUG - 3306
2018-03-08 08:33:06,643 - sch_me - ERROR - a_dict["failed_connect_count = "]3
2018-03-08 08:33:06,644 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 08:33:06,645 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 08:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 08:33:06,646 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 08:33:06,647 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 08:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:41:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 08:41:06,685 - sch_me - DEBUG - 2018-03-08 08:41:06.679493 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 08:41:06,695 - sch_me - INFO - in class DBAccess init
2018-03-08 08:41:06,696 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 08:41:06,696 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 08:41:06,696 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 08:41:06,697 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 08:41:06,697 - sch_me - DEBUG - 3306
2018-03-08 08:41:06,702 - sch_me - ERROR - a_dict["failed_connect_count = "]3
2018-03-08 08:41:06,709 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 08:41:06,713 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:55:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 08:41:06,714 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 08:41:06,715 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:55:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 08:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 08:43:06,724 - sch_me - DEBUG - 2018-03-08 08:43:06.724142 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 08:43:06,725 - sch_me - INFO - in class DBAccess init
2018-03-08 08:43:06,725 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 08:43:06,726 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 08:43:06,726 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 08:43:06,726 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 08:43:06,726 - sch_me - DEBUG - 3306
2018-03-08 08:43:06,727 - sch_me - ERROR - a_dict["failed_connect_count = "]4
2018-03-08 08:43:06,727 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 08:43:06,728 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 08:53:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 08:43:06,730 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 08:43:06,731 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 08:53:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:55:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 08:53:06,771 - sch_me - DEBUG - 2018-03-08 08:53:06.766201 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 08:53:06,780 - sch_me - INFO - in class DBAccess init
2018-03-08 08:53:06,780 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 08:53:06,781 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 08:53:06,782 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 08:53:06,782 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 08:53:06,782 - sch_me - DEBUG - 3306
2018-03-08 08:53:06,788 - sch_me - ERROR - a_dict["failed_connect_count = "]5
2018-03-08 08:53:06,788 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 08:53:06,788 - sch_me - INFO - At time: 2018-03-08 08:53:06.788655 in event test fe_db_fetch_email for greenhouse
 we got a 'bad' return = no_db_connect
2018-03-08 08:53:06,789 - sch_me - DEBUG - send_email() testing send email - actual email suppressed!!!!!!!!! Subject:  test fe_db_fetch_email for greenhouse
Message body:
At time: 2018-03-08 08:53:06.788655 in event test fe_db_fetch_email for greenhouse
 we got a 'bad' return = no_db_connect
2018-03-08 08:53:06,790 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:03:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 08:53:06,791 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 08:53:06,792 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:03:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 08:55:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 08:55:06,800 - sch_me - DEBUG - 2018-03-08 08:55:06.800001 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 08:55:06,800 - sch_me - INFO - in class DBAccess init
2018-03-08 08:55:06,800 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 08:55:06,801 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 08:55:06,801 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 08:55:06,802 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 08:55:06,802 - sch_me - DEBUG - 3306
2018-03-08 08:55:06,804 - sch_me - ERROR - a_dict["failed_connect_count = "]4
2018-03-08 08:55:06,805 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 08:55:06,807 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:09:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 08:55:06,808 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 08:55:06,809 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:09:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:03:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:03:06,842 - sch_me - DEBUG - 2018-03-08 09:03:06.837381 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 09:03:06,852 - sch_me - INFO - in class DBAccess init
2018-03-08 09:03:06,853 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 09:03:06,853 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 09:03:06,854 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:03:06,854 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:03:06,854 - sch_me - DEBUG - 3306
2018-03-08 09:03:06,860 - sch_me - ERROR - a_dict["failed_connect_count = "]6
2018-03-08 09:03:06,860 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:03:06,861 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:13:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:03:06,863 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:03:06,865 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:13:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:09:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:09:06,886 - sch_me - DEBUG - 2018-03-08 09:09:06.886385 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 09:09:06,887 - sch_me - INFO - in class DBAccess init
2018-03-08 09:09:06,887 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 09:09:06,887 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 09:09:06,888 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:09:06,889 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:09:06,889 - sch_me - DEBUG - 3306
2018-03-08 09:09:06,890 - sch_me - ERROR - a_dict["failed_connect_count = "]5
2018-03-08 09:09:06,891 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:09:06,891 - sch_me - INFO - At time: 2018-03-08 09:09:06.891207 in event test fe_db_fetch_email for rootcellar
 we got a 'bad' return = no_db_connect
2018-03-08 09:09:06,892 - sch_me - DEBUG - send_email() testing send email - actual email suppressed!!!!!!!!! Subject:  test fe_db_fetch_email for rootcellar
Message body:
At time: 2018-03-08 09:09:06.891207 in event test fe_db_fetch_email for rootcellar
 we got a 'bad' return = no_db_connect
2018-03-08 09:09:06,893 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:09:06,894 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:09:06,895 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:13:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:13:06,908 - sch_me - DEBUG - 2018-03-08 09:13:06.908936 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 09:13:06,909 - sch_me - INFO - in class DBAccess init
2018-03-08 09:13:06,910 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 09:13:06,910 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 09:13:06,911 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:13:06,911 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:13:06,912 - sch_me - DEBUG - 3306
2018-03-08 09:13:06,913 - sch_me - ERROR - a_dict["failed_connect_count = "]7
2018-03-08 09:13:06,914 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:13:06,915 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:13:06,915 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:13:06,916 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:23:06,956 - sch_me - DEBUG - 2018-03-08 09:23:06.951627 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 09:23:06,966 - sch_me - INFO - in class DBAccess init
2018-03-08 09:23:06,968 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 09:23:06,968 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 09:23:06,969 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:23:06,969 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:23:06,970 - sch_me - DEBUG - 3306
2018-03-08 09:23:06,975 - sch_me - ERROR - a_dict["failed_connect_count = "]8
2018-03-08 09:23:06,981 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:23:06,982 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:23:06,985 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:23:06,987 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:23:16,989 - sch_me - DEBUG - 2018-03-08 09:23:16.989329 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 09:23:16,989 - sch_me - INFO - in class DBAccess init
2018-03-08 09:23:16,990 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 09:23:16,990 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 09:23:16,990 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:23:16,991 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:23:16,991 - sch_me - DEBUG - 3306
2018-03-08 09:23:16,994 - sch_me - ERROR - a_dict["failed_connect_count = "]6
2018-03-08 09:23:16,995 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:23:16,996 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:37:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:23:16,996 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:23:16,997 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:37:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:33:07,037 - sch_me - DEBUG - 2018-03-08 09:33:07.030838 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 09:33:07,050 - sch_me - INFO - in class DBAccess init
2018-03-08 09:33:07,051 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 09:33:07,052 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 09:33:07,053 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:33:07,053 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:33:07,054 - sch_me - DEBUG - 3306
2018-03-08 09:33:07,060 - sch_me - ERROR - a_dict["failed_connect_count = "]9
2018-03-08 09:33:07,068 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:33:07,073 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:33:07,074 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:33:07,075 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:37:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:37:07,090 - sch_me - DEBUG - 2018-03-08 09:37:07.090442 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 09:37:07,091 - sch_me - INFO - in class DBAccess init
2018-03-08 09:37:07,091 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 09:37:07,091 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 09:37:07,092 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:37:07,092 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:37:07,092 - sch_me - DEBUG - 3306
2018-03-08 09:37:07,094 - sch_me - ERROR - a_dict["failed_connect_count = "]7
2018-03-08 09:37:07,095 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:37:07,096 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:51:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:37:07,096 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:37:07,097 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:51:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:43:07,118 - sch_me - DEBUG - 2018-03-08 09:43:07.117402 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 09:43:07,124 - sch_me - INFO - in class DBAccess init
2018-03-08 09:43:07,125 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 09:43:07,126 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 09:43:07,126 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:43:07,127 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:43:07,127 - sch_me - DEBUG - 3306
2018-03-08 09:43:07,130 - sch_me - ERROR - a_dict["failed_connect_count = "]10
2018-03-08 09:43:07,130 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:43:07,132 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:53:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:43:07,134 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:43:07,134 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:53:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 09:51:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:51:07,162 - sch_me - DEBUG - 2018-03-08 09:51:07.162136 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 09:51:07,163 - sch_me - INFO - in class DBAccess init
2018-03-08 09:51:07,163 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 09:51:07,163 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 09:51:07,164 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:51:07,164 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 09:51:07,165 - sch_me - DEBUG - 3306
2018-03-08 09:51:07,166 - sch_me - ERROR - a_dict["failed_connect_count = "]8
2018-03-08 09:51:07,167 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:51:07,167 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:05:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 09:51:07,168 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:51:07,169 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:05:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 09:53:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:53:07,177 - sch_me - DEBUG - 2018-03-08 09:53:07.177611 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 09:53:07,178 - sch_me - INFO - in class DBAccess init
2018-03-08 09:53:07,178 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 09:53:07,179 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 09:53:07,179 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:53:07,179 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 09:53:07,180 - sch_me - DEBUG - 3306
2018-03-08 09:53:07,181 - sch_me - ERROR - a_dict["failed_connect_count = "]11
2018-03-08 09:53:07,181 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 09:53:07,182 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:03:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 09:53:07,183 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 09:53:07,184 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:03:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:05:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 10:03:07,223 - sch_me - DEBUG - 2018-03-08 10:03:07.219662 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 10:03:07,232 - sch_me - INFO - in class DBAccess init
2018-03-08 10:03:07,233 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 10:03:07,234 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 10:03:07,234 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:03:07,234 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:03:07,235 - sch_me - DEBUG - 3306
2018-03-08 10:03:07,239 - sch_me - ERROR - a_dict["failed_connect_count = "]12
2018-03-08 10:03:07,240 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 10:03:07,247 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:13:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 10:03:07,249 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 10:03:07,251 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:13:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:05:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 10:05:07,259 - sch_me - DEBUG - 2018-03-08 10:05:07.259486 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 10:05:07,260 - sch_me - INFO - in class DBAccess init
2018-03-08 10:05:07,260 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 10:05:07,260 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 10:05:07,261 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 10:05:07,261 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 10:05:07,262 - sch_me - DEBUG - 3306
2018-03-08 10:05:07,265 - sch_me - ERROR - a_dict["failed_connect_count = "]9
2018-03-08 10:05:07,266 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 10:05:07,267 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:19:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 10:05:07,268 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 10:05:07,269 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:19:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:13:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 10:13:07,303 - sch_me - DEBUG - 2018-03-08 10:13:07.297395 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 10:13:07,313 - sch_me - INFO - in class DBAccess init
2018-03-08 10:13:07,314 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 10:13:07,316 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 10:13:07,316 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:13:07,316 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:13:07,317 - sch_me - DEBUG - 3306
2018-03-08 10:13:07,323 - sch_me - ERROR - a_dict["failed_connect_count = "]13
2018-03-08 10:13:07,323 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 10:13:07,325 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 10:13:07,332 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 10:13:07,333 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:19:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 10:19:07,355 - sch_me - DEBUG - 2018-03-08 10:19:07.355002 >>running event test fe_db_fetch_email for rootcellar parm: rootcellar
2018-03-08 10:19:07,355 - sch_me - INFO - in class DBAccess init
2018-03-08 10:19:07,355 - sch_me - INFO - DBAccess try a connection to 192.168.0.181
2018-03-08 10:19:07,356 - sch_me - DEBUG - a_dict_name: rootcellar
2018-03-08 10:19:07,356 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 10:19:07,356 - sch_me - DEBUG - db_host: 192.168.0.181
2018-03-08 10:19:07,356 - sch_me - DEBUG - 3306
2018-03-08 10:19:07,357 - sch_me - ERROR - a_dict["failed_connect_count = "]10
2018-03-08 10:19:07,358 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 10:19:07,358 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 10:19:07,359 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 10:19:07,360 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:23:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 10:23:07,375 - sch_me - DEBUG - 2018-03-08 10:23:07.375292 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 10:23:07,376 - sch_me - INFO - in class DBAccess init
2018-03-08 10:23:07,376 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 10:23:07,377 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 10:23:07,377 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:23:07,378 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:23:07,378 - sch_me - DEBUG - 3306
2018-03-08 10:23:07,380 - sch_me - ERROR - a_dict["failed_connect_count = "]14
2018-03-08 10:23:07,381 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 10:23:07,383 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 10:23:07,384 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 10:23:07,385 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
test fe_db_fetch_email for rootcellar a_parameter_dict_name: rootcellar next_run_time   2018-03-08 10:33:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:14:00
2018-03-08 10:33:07,423 - sch_me - DEBUG - 2018-03-08 10:33:07.423930 >>running event test fe_db_fetch_email for greenhouse parm: greenhouse
2018-03-08 10:33:07,425 - sch_me - INFO - in class DBAccess init
2018-03-08 10:33:07,425 - sch_me - INFO - DBAccess try a connection to 192.168.0.189
2018-03-08 10:33:07,426 - sch_me - DEBUG - a_dict_name: greenhouse
2018-03-08 10:33:07,426 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:33:07,426 - sch_me - DEBUG - db_host: 192.168.0.189
2018-03-08 10:33:07,427 - sch_me - DEBUG - 3306
2018-03-08 10:33:07,428 - sch_me - ERROR - a_dict["failed_connect_count = "]15
2018-03-08 10:33:07,428 - sch_me - ERROR - a_dict["max_connect_count = "]4
2018-03-08 10:33:07,430 - sch_me - DEBUG - updated eventtest fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1
reschedule_arg_2:  0:10:00
2018-03-08 10:33:07,431 - sch_me - DEBUG - erf_reschedule_deltat_t done
2018-03-08 10:33:07,431 - sch_me - DEBUG - ScheduledEventList2
test fe_db_fetch_email for greenhouse a_parameter_dict_name: greenhouse next_run_time   2018-03-08 10:43:00
event_function:  <bound method ScheduledEventList.ef_db_fetch_email of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_function:  <bound method ScheduledEventList.erf_reschedule_deltat_t of <schedule_me_helper.ScheduledEventList object at 0x000001C5B16462B0>>
reschedule_arg_1:  -1







################################################################################
# Makefile                                                                     #
#                                                                              #
# Description: This file contains the make rules for Recitation 1.             #
#                                                                              #
# Authors: Athula Balachandran <abalacha@cs.cmu.edu>,                          #
#          Wolf Richter <wolf@cs.cmu.edu>                                      #
#                                                                              #
################################################################################

default: echo_server echo_client

echo_server:
	@gcc echo_server.c -o echo_server -Wall

echo_client:
	@gcc echo_client.c -o echo_client -Wall

clean:
	@rm echo_server echo_client

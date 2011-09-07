################################################################################
# Makefile                                                                     #
#                                                                              #
# Description: This file contains the make rules for Recitation 1.             #
#                                                                              #
# Authors: Athula Balachandran <abalacha@cs.cmu.edu>,                          #
#          Wolf Richter <wolf@cs.cmu.edu>                                      #
#                                                                              #
################################################################################

SERVER_SRC = echo_server.c
CLIENT_SRC = echo_client.c
OPTIONS = -Wall

default: echo_server echo_client

echo_server:
	@gcc $(SERVER_SRC) -o echo_server $(OPTIONS)

echo_client:
	@gcc $(CLIENT_SRC) -o echo_client $(OPTIONS)

clean:
	@rm echo_server echo_client

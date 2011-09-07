#include <stdio.h>
#include <stdlib.h>
#include "select_engine.h"
#include "http_parser.h"
#include "logging.h"

#define USAGE "\nUsage: %s <PORT> <LOG_FILE> <LOCK_FILE>\n\n"

int main(int argc, char* argv[])
{
        int port;
        char* flog, * flock;

        if (argc < 4)
        {
                fprintf(stdout, USAGE, argv[0]);
                return EXIT_FAILURE;
        }

        port = atoi(argv[1]);
        flog = argv[2];
        flock = argv[3];

        struct select_engine engine;
        liso_engine_create(&engine, port, flog, flock);
        liso_engine_register_http_handler(&engine, parser_http_handler);
        liso_engine_register_http_disconnect_handler(&engine, parser_disconnect_handler);

        liso_logging_log("liso", "main", "Starting Liso server on port %d", port);

        return liso_engine_event_loop(&engine);
}


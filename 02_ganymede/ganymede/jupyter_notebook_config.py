c.NotebookApp.nbserver_extensions = {
    'ganymede.ganymede': True,
    'jupyter_nbgallery': True
}
c.NotebookApp.allow_origin = 'https://nb.gallery'

from ganymede.ganymede import GanymedeHandler
import logstash
import os
if {"L41_LOGSTASH_HOST", "L41_GANYMEDE_PORT"} < set(os.environ):
    GanymedeHandler.handlers = [
        logstash.TCPLogstashHandler(
            os.environ["L41_LOGSTASH_HOST"],
            os.environ["L41_GANYMEDE_PORT"],
            version=1,
        )
    ]

GanymedeHandler.include_filepath = True

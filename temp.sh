# use ffmpeg to ingest file/stream/device to SRS
# @see https://github.com/ossrs/srs/wiki/v1_CN_SampleIngest
# @see full.conf for detail config.

listen              1935;
max_connections     1000;
daemon              off;
srs_log_tank        console;
vhost __defaultVhost__ {
    ingest temp {
        enabled      on;
        input {
            type    stream;
            url     rtsp://192.168.8.67:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif;
        }
        ffmpeg      ./objs/ffmpeg/bin/ffmpeg;
        engine {
            enabled         off;
            output          rtmp://127.0.0.1:[port]/live?vhost=[vhost]/192.168.39.40;
        }
        engine {
            enabled         off;
            output          rtmp://127.0.0.1:[port]/live?vhost=[vhost]/192.168.39.41;
        }
        engine {
            enabled         off;
            output          rtmp://127.0.0.1:[port]/live?vhost=[vhost]/192.168.39.42;
        }
    }
}
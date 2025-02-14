FRAME_INFO_FIELDS = [
    "frame_info.time_delta",
    "frame_info.time_delta_displayed",
    "frame_info.time_epoch",
    "frame_info.time_relative",
    "frame_info.cap_len",
    "frame_info.encap_type",
    "frame_info.ignored",
    "frame_info.len",
    "frame_info.marked",
    "frame_info.number",
    "frame_info.offset_shift"
]

STACK_FIELDS = [
    "eth.src",
    "eth.dst",
    "ip.src",
    "ip.dst",
    "tcp.srcport",
    "tcp.dstport"
]

MQTT_FIELDS = [
    "mqtt.clientid",
    "mqtt.clientid_len",
    "mqtt.conack.flags",
    "mqtt.conack.flags.reserved",
    "mqtt.conack.flags.sp",
    "mqtt.conack.val",
    "mqtt.conflag.cleansess",
    "mqtt.conflag.passwd",
    "mqtt.conflag.qos",
    "mqtt.conflag.reserved",
    "mqtt.conflag.retain",
    "mqtt.conflag.uname",
    "mqtt.conflag.willflag",
    "mqtt.conflags",
    "mqtt.dupflag",
    "mqtt.hdrflags",
    "mqtt.kalive",
    "mqtt.len",
    "mqtt.msg",
    "mqtt.msgid",
    "mqtt.msgtype",
    "mqtt.passwd",
    "mqtt.passwd_len",
    "mqtt.proto_len",
    "mqtt.protoname",
    "mqtt.qos",
    "mqtt.retain",
    "mqtt.sub.qos",
    "mqtt.suback.qos",
    "mqtt.topic",
    "mqtt.topic_len",
    "mqtt.username",
    "mqtt.username_len",
    "mqtt.ver",
    "mqtt.willmsg",
    "mqtt.willmsg_len",
    "mqtt.willtopic",
    "mqtt.willtopic_len"
]

def get_fields() -> list[str]:
    fields: list[str] = []
    fields += FRAME_INFO_FIELDS
    fields += STACK_FIELDS
    fields += MQTT_FIELDS
    return fields
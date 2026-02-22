from enum import StrEnum


class BPMNTag(StrEnum):
    START_EVENT = "startEvent"
    END_EVENT = "endEvent"
    INTERMEDIATE_THROW_EVENT = "intermediateThrowEvent"
    TASK = "task"
    USER_TASK = "userTask"
    MANUAL_TASK = "manualTask"
    RECEIVE_TASK = "receiveTask"
    SCRIPT_TASK = "scriptTask"
    SEND_TASK = "sendTask"
    SERVICE_TASK = "serviceTask"
    EXCLUSIVE_GATEWAY = "exclusiveGateway"
    INCLUSIVE_GATEWAY = "inclusiveGateway"
    PARALLEL_GATEWAY = "parallelGateway"
    SEQUENCE_FLOW = "sequenceFlow"
    SUB_PROCESS = "subProcess"

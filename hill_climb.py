from db import update_global, get_member_data

def hill_climb_algorithm(member):
    member_data = get_member_data(member)
    # TODO: Implement this method based in
    # https://github.com/fogbow/fogbow-mono-manager/blob/f7be7534914d75f340d5322af7092268ebb3159c/src/main/java/org/fogbowcloud/manager/core/plugins/capacitycontroller/fairnessdriven/HillClimbingAlgorithm.java#L40
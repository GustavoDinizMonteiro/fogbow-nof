from implementations import implementation

def create_local(request, path):
    return implementation.create_local(request, path)


def create_remote(request, path):
    return implementation.create_remote(request, path)
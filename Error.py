def ApproximateError(present, previous):
    return abs(present - previous)
 
def RelativeApproximateError(present, previous):
    return ApproximateError(present, previous)/present
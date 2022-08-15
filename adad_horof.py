def adad_horof(s):
    horof={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    final=""
    adad=str(s)
    for x in adad:
        final=final+horof[x]+" "
    final=final.rstrip(" ")
    return final

print(adad_horof(4562))
        

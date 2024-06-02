
def nnf(dl_formula):
    if(len(dl_formula)<=2):
        return dl_formula
    
    dl_formula=dl_formula.replace("22", "")
    
    extra_bracket=True
    num_bracket=0
    while(dl_formula[0]=="(" and dl_formula[-1]==")" and extra_bracket):
        for i in range(len(dl_formula)):
            if(dl_formula[i]=="("):
                num_bracket+=1
            elif(dl_formula[i]==")"):
                num_bracket-=1
                if(num_bracket==0 and i!=len(dl_formula)-1):
                    extra_bracket=False
                    break
        if(extra_bracket):
            dl_formula=dl_formula[1:len(dl_formula)-1]
        else:
            break

    num_bracket=0
    sub_formula1_begin_index=0
    sub_formula1_operator_index=0
    sub_formula1_end_index=0
    sub_formula1_iterate=True
    sub_formula2_begin_index=0
    sub_formula2_end_index=0
    
    for i in range(len(dl_formula)):
        if(dl_formula[i]=="("):
            num_bracket+=1
            if(num_bracket==1):
                if(sub_formula1_iterate):
                    sub_formula1_begin_index=i+1
                else:
                    sub_formula2_begin_index=i+1
        elif(dl_formula[i]==")"):
            num_bracket-=1
            if(num_bracket==0):
                if(sub_formula1_iterate):
                    sub_formula1_end_index=i-1
                    sub_formula1_iterate=False
                else:
                    sub_formula2_end_index=i-1
        elif(dl_formula[i].isdigit() and sub_formula1_iterate and dl_formula[i] not in ["2", "5", "6"]):
            sub_formula1_operator_index=i

    if(sub_formula1_begin_index==0):
        if(dl_formula[0]=="2" and dl_formula[1] in ["5", "6"]):
            if(dl_formula[1]=="5"):
                return "6"+dl_formula[2:4]+"2"+dl_formula[4]
            elif(dl_formula[1]=="6"):
                return "5"+dl_formula[2:4]+"2"+dl_formula[4]
        elif(dl_formula[sub_formula1_operator_index]=="1"):
            return nnf(dl_formula[:sub_formula1_operator_index])+"1"+nnf(dl_formula[sub_formula1_operator_index+1:])
        elif(dl_formula[sub_formula1_operator_index]=="0"):
            return nnf(dl_formula[:sub_formula1_operator_index])+"0"+nnf(dl_formula[sub_formula1_operator_index+1:])
        elif(dl_formula[sub_formula1_operator_index]=="3"):
            return nnf("2"+dl_formula[:sub_formula1_operator_index])+"1"+nnf(dl_formula[sub_formula1_operator_index+1:])
        elif(dl_formula[sub_formula1_operator_index]=="4"):
            return "("+nnf("2"+dl_formula[:sub_formula1_operator_index]+"1"+dl_formula[sub_formula1_operator_index+1:])+")0("+nnf(dl_formula[:sub_formula1_operator_index]+"12"+dl_formula[sub_formula1_operator_index+1:])+")"
        else:
            return dl_formula
    elif(sub_formula2_begin_index==0):
        if(dl_formula[len(dl_formula)-1]==")"):
            if(sub_formula1_begin_index-2==0):
                if(dl_formula[sub_formula1_begin_index-2]=="2"):
                    if(dl_formula[sub_formula1_operator_index]=="0"):
                        return nnf("2"+dl_formula[sub_formula1_begin_index:sub_formula1_operator_index])+"1"+nnf("2"+dl_formula[sub_formula1_operator_index+1:sub_formula1_end_index+1])
                    elif(dl_formula[sub_formula1_operator_index]=="1"):
                        return nnf("2"+dl_formula[sub_formula1_begin_index:sub_formula1_operator_index])+"0"+nnf("2"+dl_formula[sub_formula1_operator_index+1:sub_formula1_end_index+1])
                    elif(dl_formula[sub_formula1_operator_index]=="3"):
                        return nnf(dl_formula[sub_formula1_begin_index:sub_formula1_operator_index])+"0"+nnf("2"+dl_formula[sub_formula1_operator_index+1:sub_formula1_end_index+1])
                    elif(dl_formula[sub_formula1_operator_index]=="4"):
                        return "("+nnf(dl_formula[sub_formula1_begin_index:sub_formula1_operator_index])+"0"+nnf(dl_formula[sub_formula1_operator_index+1:sub_formula1_end_index+1])+")1("+nnf("2"+dl_formula[sub_formula1_begin_index:sub_formula1_operator_index])+"0"+nnf("2"+dl_formula[sub_formula1_operator_index+1:sub_formula1_end_index+1])+")"
            elif(sub_formula1_begin_index-4==0):
                if(dl_formula[sub_formula1_begin_index-2]=="."):
                    if(dl_formula[sub_formula1_begin_index-4] in ["5", "6"]):
                        return dl_formula[:sub_formula1_begin_index-1]+nnf(dl_formula[sub_formula1_begin_index:sub_formula1_end_index+1])
            elif(sub_formula1_begin_index-5==0):
                if(dl_formula[sub_formula1_begin_index-2]=="."):
                    if(dl_formula[sub_formula1_begin_index-5]=="2"):
                        if(dl_formula[sub_formula1_begin_index-4]=="5"):
                            return "6"+dl_formula[2:4]+nnf("2("+dl_formula[sub_formula1_begin_index:sub_formula1_end_index+1]+")")
                        elif(dl_formula[sub_formula1_begin_index-4]=="6"):
                            return "5"+dl_formula[2:4]+nnf("2("+dl_formula[sub_formula1_begin_index:sub_formula1_end_index+1]+")")
        else:
            if(dl_formula[sub_formula1_end_index+2]=="0"):
                return nnf(dl_formula[:sub_formula1_end_index+1]+")")+"0"+nnf(dl_formula[sub_formula1_end_index+3:])                
            elif(dl_formula[sub_formula1_end_index+2]=="1"):
                return nnf(dl_formula[:sub_formula1_end_index+1]+")")+"1"+nnf(dl_formula[sub_formula1_end_index+3:])
            elif(dl_formula[sub_formula1_end_index+2]=="3"):
                return nnf("2"+dl_formula[:sub_formula1_end_index+1]+")")+"1"+nnf(dl_formula[sub_formula1_end_index+3:])
            elif(dl_formula[sub_formula1_end_index+2]=="4"):
                return "("+nnf("2"+dl_formula[:sub_formula1_end_index+1]+")1"+dl_formula[sub_formula1_end_index+3:])+")0("+nnf(dl_formula[:sub_formula1_end_index+1]+")12("+dl_formula[sub_formula1_end_index+3:]+")")+")"
    else:
        if(dl_formula[sub_formula1_end_index+2]=="0"):
            return nnf(dl_formula[:sub_formula1_end_index+1]+")")+"0"+nnf(dl_formula[sub_formula1_end_index+3:sub_formula2_end_index+1]+")")
        elif(dl_formula[sub_formula1_end_index+2]=="1"):
            return nnf(dl_formula[:sub_formula1_end_index+1]+")")+"1"+nnf(dl_formula[sub_formula1_end_index+3:sub_formula2_end_index+1]+")")
        elif(dl_formula[sub_formula1_end_index+2]=="3"):
            return nnf("2("+dl_formula[:sub_formula1_end_index+1]+"))")+"1"+nnf(dl_formula[sub_formula1_end_index+3:sub_formula2_end_index+1]+")")
        elif(dl_formula[sub_formula1_end_index+2]=="4"):
            return "("+nnf("2"+dl_formula[:sub_formula1_end_index+1]+")1"+dl_formula[sub_formula1_end_index+3:sub_formula2_end_index+1]+")")+")0("+nnf(dl_formula[:sub_formula1_end_index+1]+")12"+dl_formula[sub_formula1_end_index+3:sub_formula2_end_index+1]+")")+")"
    
    return ""


dl_formula=input().strip()
result=nnf(dl_formula)
print(result)
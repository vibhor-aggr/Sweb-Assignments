def tableau(sign, rule, level, part, sub_part):
    if(level>2):
        return
    if(len(rule)<=1):
        return
    
    extra_bracket=True
    num_bracket=0
    while(rule[0]=="(" and rule[-1]==")" and extra_bracket):
        for i in range(len(rule)):
            if(rule[i]=="("):
                num_bracket+=1
            elif(rule[i]==")"):
                num_bracket-=1
                if(num_bracket==0 and i!=len(rule)-1):
                    extra_bracket=False
                    break
        if(extra_bracket):
            rule=rule[1:len(rule)-1]
        else:
            break


    num_bracket=0
    sub_rule1_begin_index=0
    sub_rule1_operator_index=0
    sub_rule1_end_index=0
    sub_rule1_iterate=True
    sub_rule2_begin_index=0
    sub_rule2_end_index=0
    
    for i in range(len(rule)):
        if(rule[i]=="("):
            num_bracket+=1
            if(num_bracket==1):
                if(sub_rule1_iterate):
                    sub_rule1_begin_index=i+1
                else:
                    sub_rule2_begin_index=i+1
        elif(rule[i]==")"):
            num_bracket-=1
            if(num_bracket==0):
                if(sub_rule1_iterate):
                    sub_rule1_end_index=i-1
                    sub_rule1_iterate=False
                else:
                    sub_rule2_end_index=i-1
        elif(rule[i].isdigit() and sub_rule1_iterate and rule[i]!="2"):
            sub_rule1_operator_index=i

    if(sub_rule1_begin_index==0):
        if(rule[0]=="2" and len(rule)==2):
            print(f"Level {level}")
            if(sign=="F"):
                print(f"{part}.{sub_part+1} T {rule[1]}")
                tableau("T", rule[1], level, part, sub_part+1)
            else:
                print(f"{part}.{sub_part+1} F {rule[1]}")
                tableau("F", rule[1], level, part, sub_part+1)
        elif(rule[sub_rule1_operator_index]=="0"):
            if(sign=="F"):
                print("\n", end="")
                print(f"Level {level+1}")
                print(f"{1}.{1} F {rule[:sub_rule1_operator_index]}")
                print(f"{2}.{1} F {rule[sub_rule1_operator_index+1:]}")
                tableau("F", rule[:sub_rule1_operator_index], level+1, 1, 1)
                tableau("F", rule[sub_rule1_operator_index+1:], level+1, 2, 1)
            else:
                print(f"Level {level}")
                print(f"{part}.{sub_part+1} T {rule[:sub_rule1_operator_index]}")
                print(f"{part}.{sub_part+2} T {rule[sub_rule1_operator_index+1:]}")
                sub_part=tableau("T", rule[:sub_rule1_operator_index], level, part, sub_part+2)
                tableau("T", rule[sub_rule1_operator_index+1:], level, part, sub_part+2)
        elif(rule[sub_rule1_operator_index]=="1"):
            if(sign=="F"):
                print(f"Level {level}")
                print(f"{part}.{sub_part+1} F {rule[:sub_rule1_operator_index]}")
                print(f"{part}.{sub_part+2} F {rule[sub_rule1_operator_index+1:]}")
                sub_part=tableau("F", rule[:sub_rule1_operator_index], level, part, sub_part+2)
                tableau("F", rule[sub_rule1_operator_index+1:], level, part, sub_part+2)
            else:
                print("\n", end="")
                print(f"Level {level+1}")
                print(f"{1}.{1} T {rule[:sub_rule1_operator_index]}")
                print(f"{2}.{1} T {rule[sub_rule1_operator_index+1:]}")
                tableau("T", rule[:sub_rule1_operator_index], level+1, 1, 1)
                tableau("T", rule[sub_rule1_operator_index+1:], level+1, 2, 1)
    elif(sub_rule2_begin_index==0):
        if(rule[len(rule)-1]==")"):
            if(rule[0]=="2"):
                print(f"Level {level}")
                if(sign=="F"):
                    print(f"{part}.{sub_part+1} T {rule[sub_rule1_begin_index:sub_rule1_end_index+1]}")
                    tableau("T", rule[sub_rule1_begin_index:sub_rule1_end_index+1], level, part, sub_part+1)
                else:
                    print(f"{part}.{sub_part+1} F {rule[sub_rule1_begin_index:sub_rule1_end_index+1]}")
                    tableau("F", rule[sub_rule1_begin_index:sub_rule1_end_index+1], level, part, sub_part+1)
        elif(rule[sub_rule1_end_index+2]=="0"):
            if(sign=="F"):
                print("\n", end="")
                print(f"Level {level+1}")
                print(f"{1}.{1} F {rule[sub_rule1_begin_index:sub_rule1_end_index+1]}")
                print(f"{2}.{1} F {rule[sub_rule1_end_index+3:]}")
                tableau("F", rule[sub_rule1_begin_index:sub_rule1_end_index+1], level+1, 1, 1)
                tableau("F", rule[sub_rule1_end_index+3:], level+1, 2, 1)
            else:
                print(f"Level {level}")
                print(f"{part}.{sub_part+1} T {rule[sub_rule1_begin_index:sub_rule1_end_index+1]}")
                print(f"{part}.{sub_part+2} T {rule[sub_rule1_end_index+3:]}")
                sub_part=tableau("T", rule[sub_rule1_begin_index:sub_rule1_end_index+1], level, part, sub_part+2)
                tableau("T", rule[sub_rule1_end_index+3:], level, part, sub_part+2)
        elif(rule[sub_rule1_end_index+2]=="1"):
            if(sign=="F"):
                print(f"Level {level}")
                print(f"{part}.{sub_part+1} F {rule[sub_rule1_begin_index:sub_rule1_end_index+1]}")
                print(f"{part}.{sub_part+2} F {rule[sub_rule1_end_index+3:]}")
                sub_part=tableau("F", rule[sub_rule1_begin_index:sub_rule1_end_index+1], level, part, sub_part+2)
                tableau("F", rule[sub_rule1_end_index+3:], level, part, sub_part+2)
            else:
                print("\n", end="")
                print(f"Level {level+1}")
                print(f"{1}.{1} T {rule[sub_rule1_begin_index:sub_rule1_end_index+1]}")
                print(f"{2}.{1} T {rule[sub_rule1_end_index+3:]}")
                tableau("T", rule[sub_rule1_begin_index:sub_rule1_end_index+1], level+1, 1, 1)
                tableau("T", rule[sub_rule1_end_index+3:], level+1, 2, 1)
    else:
        if(rule[sub_rule1_end_index+2]=="0"):
            if(sign=="F"):
                print("\n", end="")
                print(f"Level {level+1}")
                print(f"{1}.{1} F {rule[:sub_rule1_end_index+2]}")
                print(f"{2}.{1} F {rule[sub_rule1_end_index+3:]}")
                tableau("F", rule[:sub_rule1_end_index+2], level+1, 1, 1)
                tableau("F", rule[sub_rule1_end_index+3:], level+1, 2, 1)
            else:
                print(f"Level {level}")
                print(f"{part}.{sub_part+1} T {rule[:sub_rule1_end_index+2]}")
                print(f"{part}.{sub_part+2} T {rule[sub_rule1_end_index+3:]}")
                sub_part=tableau("T", rule[:sub_rule1_end_index+2], level, part, sub_part+2)
                tableau("T", rule[sub_rule1_end_index+3:], level, part, sub_part+2)
        elif(rule[sub_rule1_end_index+2]=="1"):
            if(sign=="F"):
                print(f"Level {level}")
                print(f"{part}.{sub_part+1} F {rule[:sub_rule1_end_index+2]}")
                print(f"{part}.{sub_part+2} F {rule[sub_rule1_end_index+3:]}")
                sub_part=tableau("F", rule[:sub_rule1_end_index+2], level, part, sub_part+2)
                tableau("F", rule[sub_rule1_end_index+3:], level, part, sub_part+2)
            else:
                print("\n", end="")
                print(f"Level {level+1}")
                print(f"{1}.{1} T {rule[:sub_rule1_end_index+2]}")
                print(f"{2}.{1} T {rule[sub_rule1_end_index+3:]}")
                tableau("T", rule[:sub_rule1_end_index+2], level+1, 1, 1)
                tableau("T", rule[sub_rule1_end_index+3:], level+1, 2, 1)

    return sub_part+1

rule=(input().strip()).split()
print("Level 0")
print(f"{1}.{1} {rule[0]} {rule[1]}")
tableau(rule[0], rule[1], 0, 1, 1)
import numpy as np



def check_for_issues(label_true, label_pred):
    if len(label_true) != len(label_pred):
        raise ValueError("The length of label_true and label_pred must be the same.")
    if len(label_true) == 0:
        raise ValueError("The length of label_true and label_pred must be greater than 0.")
    if len(label_true[0]) == 0:
        raise ValueError("The number of classes must be greater than 0.")    





def category_of_instance(label_instance_true, label_instance_pred):
    
    check_next = False
    for i in range(len(label_instance_true)):
        if label_instance_pred[i] == 1:
            if label_instance_true[i] != 1:
                check_next = True
                continue
    if check_next == False:
        return 1
    check_next = False
    
    for i in range(len(label_instance_true)):
        if label_instance_true[i] == 1:
            if label_instance_pred[i] != 1:
                check_next = True
                continue
    if check_next == False:
        return 2
    
    return 3

def normalize(matrix):
    pass







def cm(label_true, label_pred):
    cm1 = conf_mat_case_1(label_true, label_pred)
    cm2 = conf_mat_case_2(label_true, label_pred)
    cm3 = con_mat_case_3(label_true, label_pred)   
    conf_mat = cm1 + cm2 + cm3
    
    
    normalize_conf_mat = normalize(conf_mat)
    
    return conf_mat




def conf_mat_case_1(label_true, label_pred):
    check_for_issues(label_true, label_pred)
    conf_mat = np.zeros((len(label_true[0])+1, len(label_true[0])+1), dtype=int)
    num_classes = len(label_true[0])
    
    
    for i in range(len(label_true)):
        if category_of_instance(label_true[i], label_pred[i]) !=1:
            continue
        sum_true = sum(label_true[i])
        sum_pred = sum(label_pred[i])
        if sum_true == 0 and sum_pred == 0:
            conf_mat[num_classes, num_classes] += 1
        
        for j in range(num_classes):
            if label_true[i][j] == 1 and label_pred[i][j] == 1:
                conf_mat[j][j] += 1
        
        for j in range(num_classes):
            if label_true[i][j] == 1 and label_pred[i][j] == 0:
                conf_mat[j][num_classes] += 1      

    return conf_mat



def conf_mat_case_2(label_true, label_pred):
    check_for_issues(label_true, label_pred)
    conf_mat = np.zeros((len(label_true[0])+1, len(label_true[0])+1), dtype=int)
    num_classes = len(label_true[0])
    
    
    for i in range(len(label_true)):
        if category_of_instance(label_true[i], label_pred[i]) !=2:
            continue    
    
        sum_true = sum(label_true[i])
        sum_pred = sum(label_pred[i])
        if sum_true == 0 and sum_pred == 0:
            conf_mat[num_classes, num_classes] += 1
            
        for j in range(num_classes):
            if label_true[i][j] == 1 and label_pred[i][j] == 1:
                conf_mat[j][j] += 1
            
            
            
            
        for j in range(num_classes):
            if label_true[i][j] == 1:
                for k in range(num_classes):
                    if label_pred[i][k] == 1 and label_true[i][k] !=1:
                        conf_mat[j][k] +=1
        if sum_true == 0:
            for j in range(num_classes):
                if label_pred[i][j] == 1 and label_true[i][j] != 1:
                    conf_mat[num_classes][j] += 1
                    
    return conf_mat




def con_mat_case_3(label_true, label_pred):
    check_for_issues(label_true, label_pred)
    conf_mat = np.zeros((len(label_true[0])+1, len(label_true[0])+1), dtype=int)
    num_classes = len(label_true[0])
    
    
    for i in range(len(label_true)):
        if category_of_instance(label_true[i], label_pred[i]) !=3:
            continue    
    
        sum_true = sum(label_true[i])
        sum_pred = sum(label_pred[i])
        if sum_true == 0 and sum_pred == 0:
            conf_mat[num_classes, num_classes] += 1
            
        for j in range(num_classes):
            if label_true[i][j] == 1 and label_pred[i][j] == 1:
                conf_mat[j][j] += 1
    
        for j in range(num_classes):
            if label_true[i][j] == 1 and label_pred[i][j] != 1:
                for k in range(num_classes):
                    if label_pred[i][k] == 1 and label_true[i][k] != 1:
                        conf_mat[j][k] += 1
                    
                        
    return conf_mat


    

    
    
if __name__ == "__main__":
    pass
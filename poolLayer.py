
import numpy as np
import im2col

def pool(A, F, stride):
    
    F_h = F[0]
    F_w = F[1]
    A_h = A.shape[-2]
    A_w = A.shape[-1]
    A_c = A.shape[1]
    padding = A_h % 2
    out_h = int(((A_h - F_h + 2*padding) / stride) + 1)
    out_w = int(((A_w - F_w + 2*padding) / stride) + 1)
    
    A_col = im2col.im2col_indices(A, F_h, F_w, padding, stride)
    temp = np.vsplit(A_col, A_c)
    mask = np.zeros_like(temp, dtype = int)
    idx = np.zeros((len(temp),temp[0].shape[-1]), dtype = int)
    
    for i in range(len(temp)):
        idx[i] = np.argmax(temp[i], axis = 0)
        temp[i] = temp[i][idx[i], range(idx[i].size)]
        mask[i][idx[i], range(idx[i].size)] = 1
    
    max_pool = np.squeeze(temp)
    out = max_pool.reshape(1, A_c, out_h, out_w)
    mask = np.vstack(mask)
    mask = im2col.col2im_indices(mask, A.shape, F_h, F_w, padding, stride)
    
    return out, mask


def keys(self):
    all_key = []
    for i in range(len(self.data_map)):
        ## Check if there's anything at this index
        if self.data_map[i] is not None:
            ## Loop through the list at this index
            for j in range(len(self.data_map[i])):
                ## Append the key to the all_key list
                all_key.append(self.data_map[i][j][0])
    return all_key
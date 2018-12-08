with open('input', 'r') as file:
    input = file.read()

nums = input.split()
for n in range(len(nums)):
    nums[n] = int(nums[n])

class Part1:
    def __init__(self,vals):
        # pull out header
        num_children = vals[0]
        num_meta = vals[1]

        # init childrent list
        children_list = []

        # populate children recursively
        for _j in range(num_children):
            # children always start 2 in
            next_child = 2
            # but we have to add on any previous children sizes
            for c in children_list:
                next_child += c.size
            children_list.append(Part1(vals[next_child:]))

        # metadata offset is minumum 2, plus size of all children
        meta_off = 2
        for c in children_list:
            meta_off += c.size

        # now we can rip out meta data        
        metadata = list(vals[meta_off:meta_off+num_meta])

        # detertmine how big we are
        self.size = meta_off+num_meta

        # anddetermine our value by summing our meta data with our children's metadata
        self.value = sum(metadata)
        for c in children_list:
            self.value += c.value

class Part2:
    def __init__(self,vals):
        # pull out header
        num_children = vals[0]
        num_meta = vals[1]

        # init childrent list
        children_list = []

        # populate children recursively
        for _j in range(num_children):
            # children always start 2 in
            next_child = 2
            # but we have to add on any previous children sizes
            for c in children_list:
                next_child += c.size
            children_list.append(Part2(vals[next_child:]))

        # metadata offset is minumum 2, plus size of all children
        meta_off = 2
        for c in children_list:
            meta_off += c.size

        # now we can rip out meta data        
        metadata = list(vals[meta_off:meta_off+num_meta])

        # detertmine how big we are
        self.size = meta_off+num_meta

        # and we can figure out our value based on the crazy way specified
        if len(children_list) == 0:
            self.value = sum(metadata)
        else:
            value = 0
            for v in metadata:
                if v > 0 and v <= len(children_list):
                    value += children_list[v-1].value
            self.value = value

a = Part1(nums)
print("Part 1: ", a.value)
a = Part2(nums)
print("Part 2: ", a.value)


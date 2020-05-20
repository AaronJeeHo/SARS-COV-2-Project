def get_orfs(seq, minbp, nested):
    """
    Seq: Reference Genome
    minbp: Min ORF size
    nested: True: Show all ORFs
            False: Hide nested ORFs
    """

    stop_c = ['TAG', 'TAA', 'TGA']
    orf_list = []

    for frame in range(3):
        start_pos, end_pos = ([] for l in range(2))

        can_start = True
        for i in range(frame, len(seq), 3):
            codon = seq[i:i + 3]

            if codon == 'ATG' and can_start:
                start_pos.append(i)
                can_start = False
            elif codon in stop_c:
                end_pos.append(i)

                can_start = True

        end_index = 0
        last_end = end_pos[len(end_pos) - 1]
        curr_orfs = []

        for i in start_pos:  # for every start position

            if i < end_pos[end_index]:  # if start less than end
                curr_orfs.append((i, end_pos[end_index]))
            elif i > last_end:
                break
            else:
                while end_pos[end_index] < i:
                    end_index += 1
                curr_orfs.append((i, end_pos[end_index]))

        prev_end = -1
        for i in curr_orfs:
            if (i[1] - i[0]) >= minbp:
                if nested:
                    orf_list.append((i[0] + 1, i[1], frame + 1))

                elif i[1] != prev_end:
                    orf_list.append((i[0] + 1, i[1], frame + 1))
            prev_end = i[1]

    orf_list.sort(key=lambda gene: (gene[0], gene[1], gene[2]))

    #This portion only runs if we want to remove nested
    if nested is False:
        orf_overlaps = sorted(orf_list,
                              key=lambda gene: (gene[1] - gene[0]), reverse=True)

        for i in orf_overlaps:
            orf_list[:] = [g for g in orf_list if g == i
                           or g[0] < i[0] or g[1] > i[1]]

    return orf_list

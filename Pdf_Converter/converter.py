import PyPDF2
import pandas as pd


def read_to_string(pdfReader_obj):
    all_in_one = ''
    for page_no in range(pdfReader_obj.getNumPages()):
        pageObj_single = pdfReader_obj.getPage(page_no)
        pageone_text_single = pageObj_single.extractText()
        all_in_one = all_in_one + pageone_text_single
    return all_in_one


def get_name(single_student_text, name_start_index):
    name_str = single_student_text[name_start_index:40]
    full_name = name_str.strip()
    return full_name


def get_sub_list(sem_no, single_student_text):
    list_of_subjects = []
    if sem_no == 1:
        list_of_subjects = [' 101 ', ' 102 ', ' 103 ', ' 104 ', ' 105 ',
                            ' 106 ', ' 107 ', ' 108 ', ' 109 ', ' 110 ', ' 111 ', ' 191 ', ' 192 ']
    elif sem_no == 2:
        list_of_subjects = [' 101 ', ' 102 ', ' 103 ', ' 104 ', ' 105 ', ' 106 ', ' 107 ', ' 108 ', ' 109 ', ' 110 ', ' 111 ', ' 191 ',
                            ' 192 ', ' 201 ', ' 202 ', ' 203 ', ' 204 ', ' 205 ', ' 206 ', ' 207 ', ' 208 ', ' 209 ', ' 210 ', ' 211 ', ' 291 ', ' 292 ']
    elif sem_no == 3:
        if single_student_text.find(' 324A ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ',
                                ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324A ', ' 325A ', ' 326A ', ' 327A ', ' 328A ', ' 329A ', ' 392 ', ' 394 ']
        elif single_student_text.find(' 324B ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ',
                                ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324B ', ' 325B ', ' 326B ', ' 327B ', ' 328B ', ' 329B ', ' 392 ', ' 394 ']
        elif single_student_text.find(' 324C ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ',
                                ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324C ', ' 325C ', ' 326C ', ' 327C ', ' 328C ', ' 329C ', ' 392 ', ' 394 ']
    elif sem_no == 4:
        if single_student_text.find(' 424A ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ',
                                ' 321 ', ' 322 ', ' 323 ', ' 324A ', ' 325A ', ' 326A ', ' 327A ', ' 328A ', ' 329A ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424A ', ' 425A ', ' 426A ', ' 427A ', ' 428A ', ' 429A ', ' 492 ', ' 494 ']
        elif single_student_text.find(' 424B ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ',
                                ' 321 ', ' 322 ', ' 323 ', ' 324B ', ' 325B ', ' 326B ', ' 327B ', ' 328B ', ' 329B ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424B ', ' 425B ', ' 426B ', ' 427B ', ' 428B ', ' 429B ', ' 492 ', ' 494 ']
        elif single_student_text.find(' 424C ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ',
                                ' 321 ', ' 322 ', ' 323 ', ' 324C ', ' 325C ', ' 326C ', ' 327C ', ' 328C ', ' 329C ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424C ', ' 425C ', ' 426C ', ' 427C ', ' 428C ', ' 429C ', ' 492 ', ' 494 ']
    elif sem_no == 5:
        if single_student_text.find(' 524A ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324A ',
                                ' 325A ', ' 326A ', ' 327A ', ' 328A ', ' 329A ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424A ', ' 425A ', ' 426A ', ' 427A ', ' 428A ', ' 429A ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' 524A ', ' 525A ', ' 526A ', ' 527A ', ' 528A ', ' 529A ']
        elif single_student_text.find(' 524B ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324B ',
                                ' 325B ', ' 326B ', ' 327B ', ' 328B ', ' 329B ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424B ', ' 425B ', ' 426B ', ' 427B ', ' 428B ', ' 429B ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' 524B ', ' 525B ', ' 526B ', ' 527B ', ' 528B ', ' 529B ']
        elif single_student_text.find(' 524C ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324C ',
                                ' 325C ', ' 326C ', ' 327C ', ' 328C ', ' 329C ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424C ', ' 425C ', ' 426C ', ' 427C ', ' 428C ', ' 429C ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' 524C ', ' 525C ', ' 526C ', ' 527C ', ' 528C ', ' 529C ']
    elif sem_no == 6:
        if single_student_text.find(' 324A ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324A ', ' 325A ', ' 326A ',
                                ' 327A ', ' 328A ', ' 329A ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424A ', ' 425A ', ' 426A ', ' 427A ', ' 428A ', ' 429A ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' 524A ', ' 525A ', ' 526A ', ' 527A ', ' 528A ', ' 529A ', ' 621 ', ' 622 ', ' 623 ']
        elif single_student_text.find(' 324B ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324B ', ' 325B ', ' 326B ',
                                ' 327B ', ' 328B ', ' 329B ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424B ', ' 425B ', ' 426B ', ' 427B ', ' 428B ', ' 429B ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' 524B ', ' 525B ', ' 526B ', ' 527B ', ' 528B ', ' 529B ', ' 621 ', ' 622 ', ' 623 ']
        elif single_student_text.find(' 324C ') != -1:
            list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' 324C ', ' 325C ', ' 326C ',
                                ' 327C ', ' 328C ', ' 329C ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' 424C ', ' 425C ', ' 426C ', ' 427C ', ' 428C ', ' 429C ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' 524C ', ' 525C ', ' 526C ', ' 527C ', ' 528C ', ' 529C ', ' 621 ', ' 622 ', ' 623 ']
    return list_of_subjects

# list of subject codes should be provieded depending upon the year


def get_df_sublist(sem_no):
    if sem_no == 3:
        list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ',
                            ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' Group ', ' 324 ', ' 325 ', ' 326 ', ' 327 ', ' 328 ', ' 329 ', ' 392 ', ' 394 ']
    elif sem_no == 4:
        list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ',
                            ' 321 ', ' 322 ', ' 323 ', ' Group ', ' 324 ', ' 325 ', ' 326 ', ' 327 ', ' 328 ', ' 329 ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' Group ', ' 424 ', ' 425 ', ' 426 ', ' 427 ', ' 428 ', ' 429 ', ' 492 ', ' 494 ']
    elif sem_no == 5:
        list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' Group ', ' 324 ',
                            ' 325 ', ' 326 ', ' 327 ', ' 328 ', ' 329 ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' Group ', ' 424 ', ' 425 ', ' 426 ', ' 427 ', ' 428 ', ' 429 ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' Group ', ' 524 ', ' 525 ', ' 526 ', ' 527 ', ' 528 ', ' 529 ']
    elif sem_no == 6:
        list_of_subjects = [' 121 ', ' 122 ', ' 123 ', ' 124 ', ' 125 ', ' 126 ', ' 127 ', ' 128 ', ' 129 ', ' 191 ', ' 192 ', ' 221 ', ' 222 ', ' 223 ', ' 224 ', ' 225 ', ' 226 ', ' 227 ', ' 228 ', ' 229 ', ' 291 ', ' 292 ', ' 321 ', ' 322 ', ' 323 ', ' Group ', ' 324 ', ' 325 ', ' 326 ',
                            ' 327 ', ' 328 ', ' 329 ', ' 392 ', ' 394 ', ' 421 ', ' 422 ', ' 423 ', ' Group ', ' 424 ', ' 425 ', ' 426 ', ' 427 ', ' 428 ', ' 429 ', ' 492 ', ' 494 ', ' 521 ', ' 522 ', ' 523 ', ' Group ', ' 524 ', ' 525 ', ' 526 ', ' 527 ', ' 528 ', ' 529 ', ' 621 ', ' 622 ', ' 623 ']
    return list_of_subjects


def gen_seatno_list(input_start_seat_no, input_end_seat_no):
    list_of_seat_no = list(range(input_start_seat_no, input_end_seat_no+1))
    list_of_seat_no_str = []
    for item_losn in list_of_seat_no:
        list_of_seat_no_str.append(str(item_losn))
    return list_of_seat_no_str


def converter(pdfReader_obj, input_start_seat_no, input_end_seat_no, sem_no):
    to_single_string = read_to_string(pdfReader_obj)
    seat_no_list = gen_seatno_list(input_start_seat_no, input_end_seat_no)
    all_students_marks = []
    # looping through the list of seat numbers
    for seat_no_index in range(0, len(seat_no_list)):
        # taking the seat number index
        start_seat_no = seat_no_list[seat_no_index]
        # for handing the condition of last seat number of list
        if start_seat_no != seat_no_list[-1]:
            upto_seat_no = seat_no_list[seat_no_index+1]
        else:
            upto_seat_no = ''

        start_seat_no_index = to_single_string.find(start_seat_no)
        # for handling the last seat number index i.e upto where to look
        if upto_seat_no != '':
            end_seat_no_index = to_single_string.find(upto_seat_no)
        else:
            end_seat_no_index = None

        # taking the block of marks of specific student
        single_student_text = to_single_string[start_seat_no_index:end_seat_no_index]

        list_of_individual = []

        seat_no_individual = ''
        seat_no_individual = single_student_text[:5]
        list_of_individual.append([seat_no_individual])

        name_start_index = len(seat_no_individual)+2

        full_name = get_name(single_student_text, name_start_index)

        list_of_individual.append([full_name])

        list_of_subjects = get_sub_list(sem_no, single_student_text)

        # looping through the subject list for collectiong the marks
        for i in range(0, len(list_of_subjects)):
            sub_code_start_index = single_student_text.find(
                list_of_subjects[i])
            if sub_code_start_index == (single_student_text.find(list_of_subjects[-1])):
                sub_code_end_index = sub_code_start_index+29
            else:
                sub_code_end_index = single_student_text.find(
                    list_of_subjects[i+1])
            sub_marks_string = single_student_text[(
                sub_code_start_index+7):sub_code_end_index]

            list_of_marks = sub_marks_string.split(' ')
            cleaned_marks = []
            # ,' 324C ',' 424B ',' 524C '
            if list_of_subjects[i] in [' 324A ', ' 424A ', ' 524A ']:
                cleaned_marks.insert(0, ' A ')
            elif list_of_subjects[i] in [' 324B ', ' 424B ', ' 524B ']:
                cleaned_marks.insert(0, ' B ')
            elif list_of_subjects[i] in [' 324C ', ' 424C ', ' 524C ']:
                cleaned_marks.insert(0, ' C ')
            for list_item in list_of_marks:
                if list_item.strip() and not('---' in list_item) and not('!' in list_item):
                    cleaned_marks.append(list_item)
            while ((len(cleaned_marks) > 6) and not((' A ' in cleaned_marks) or (' B ' in cleaned_marks) or (' C ' in cleaned_marks))):
                cleaned_marks.pop()

            list_of_individual.append(cleaned_marks)
        all_students_marks.append(list_of_individual)
    for individual_student in all_students_marks:
        individual_student_prepared = []
        for individual_student_list_item in individual_student:
            #         print(individual_student_list_item)
            if sem_no == 6 or sem_no == 5:
                if len(individual_student_list_item) == 4 and ' * ' not in individual_student_list_item:
                    individual_student_list_item.insert(1, ' ')
                    individual_student_list_item.insert(1, ' ')
                if '*' not in individual_student_list_item and len(individual_student_list_item) == 5:
                    individual_student_list_item.insert(2, ' ')
                if (' A ' in individual_student_list_item) and not('*' in individual_student_list_item) and len(individual_student_list_item) == 6:
                    individual_student_list_item.insert(3, ' ')
                if (' B ' in individual_student_list_item) and not('*' in individual_student_list_item) and len(individual_student_list_item) == 6:
                    individual_student_list_item.insert(3, ' ')
                if (' C ' in individual_student_list_item) and not('*' in individual_student_list_item) and len(individual_student_list_item) == 6:
                    individual_student_list_item.insert(3, ' ')
                if '*' in individual_student_list_item and len(individual_student_list_item) == 5:
                    individual_student_list_item.insert(1, ' ')

            else:
                if len(individual_student_list_item) > 1 and len(individual_student_list_item) <= 5:
                    if '*' not in individual_student_list_item and len(individual_student_list_item) == 4:
                        individual_student_list_item.insert(1, ' ')
                        individual_student_list_item.insert(1, ' ')
                    if '*' not in individual_student_list_item and len(individual_student_list_item) == 5:
                        individual_student_list_item.insert(2, ' ')
                    if '*' in individual_student_list_item and len(individual_student_list_item) == 5:
                        individual_student_list_item.insert(1, ' ')
            if '$' in individual_student_list_item:
                #             print(individual_student_list_item)
                if len(individual_student_list_item) == 7:
                    individual_student_list_item[4] = individual_student_list_item[4] + \
                        individual_student_list_item[5]
                    individual_student_list_item.remove('$')
                    individual_student_list_item.insert(3, ' ')
                elif len(individual_student_list_item) == 6:
                    individual_student_list_item[4] = individual_student_list_item[3] + \
                        individual_student_list_item[4]
                    individual_student_list_item.remove('P')
                    individual_student_list_item.insert(2, ' ')
    #             print(individual_student_list_item)
            individual_student_prepared.append(individual_student_list_item)
    marks_df = pd.DataFrame()

    if sem_no > 2:                     # get new sublist for df only if sem grt than 2
        list_of_subjects = get_df_sublist(sem_no)

    list_of_columns = []

    for each_sub in list_of_subjects:
        list_sub_addons = ['_INT', '_EXT',
                           '_CUR_SUB', '_TOTAL', '_GRADE', '_CRD']
        if each_sub == ' Group ':
            list_of_columns.append(' Group ')
        else:
            for list_sub_addons_item in list_sub_addons:
                marks_type = each_sub + list_sub_addons_item
                list_of_columns.append(marks_type)

    list_final_columns = ['seat no', 'name of student'] + list_of_columns
    marks_df = pd.DataFrame(columns=list_final_columns)

    # for part_of_all_students in all_students_marks_inpart:

    for individual_student in all_students_marks:
        individual_student_single_prepared = []
        for individual_student_item in individual_student:
            for individual_student_item_1 in individual_student_item:
                individual_student_single_prepared.append(
                    individual_student_item_1)
        try:
            marks_df.loc[len(marks_df)] = individual_student_single_prepared
        except:
            print(f'incorrect entry - {individual_student_single_prepared[0]}')

    return marks_df

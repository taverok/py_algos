import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Concatenate FILE(s) to standard output.')
    parser.add_argument('file_names', help='files to concatenate', type=str, nargs='+')
    parser.add_argument('-n', '--numbers', help='number all output lines', action='store_true')
    parser.add_argument('-b', '--number-nonblank', help='number nonempty output lines, overrides -n', action='store_true')
    parser.add_argument('-s', '--squeeze-blank', help='suppress repeated empty output lines', action='store_true')
    parser.add_argument('-E', '--show-ends', help='display $ at end of each line', action='store_true')
    parser.add_argument('-T', '--show-tabs', help='display TAB characters as ^I', action='store_true')
    parser.add_argument('-A', '--show-all', help='equivalent to -ET', action='store_true')
    args = parse_args()

    if args.show_all:
        args.show_ends, args.show_tabs = True, True

    return args


def read_lines(file_names, args):
    lines = []
    for file_name in file_names:
        with open(file_name) as fh:
            prev_empty = False
            for l in fh.readlines():
                if l == '\n':
                    if prev_empty and args.squeeze_blank:
                        continue
                    prev_empty = True
                else:
                    prev_empty = False
                lines.append(l.rstrip('\n'))

    return lines


def main():
    args = parse_args()

    lines = read_lines(args.file_names, args)
    count = 0
    for l in lines:
        if args.show_ends:
            l += '$'
        if args.show_tabs:
            l = l.replace('\t', '^I')

        if args.numbers or args.number_nonblank:
            if l == '\n' and args.number_nonblank:
                print('{: >8} {}'.format(' ', l))
            else:
                count += 1
                print('{: >8} {}'.format(count, l))
        else:
            print(l)

if __name__ == '__main__':
    main()

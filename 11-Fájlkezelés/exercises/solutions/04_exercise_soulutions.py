# 4.
def file_stats(filename):
    stats = {
        'line_count': 0,
        'words_count': 0,
        'characters_length': 0
    }

    with open(filename, 'r') as f:
        for line in f:
            stats['line_count'] += 1
            stats['words_count'] += len(line.split())
            stats['characters_length'] += len(line)

    return stats


print(file_stats('statistic.txt'))

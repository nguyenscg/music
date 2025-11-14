# allow users to look up music by album, artist, or year
# if a user looks for an album: return the album name with the artist and year
# if a user looks for an artist: return all their discography with year
# if a user looks for by year, return all the albums with artist in that year

def music_data(file, search):
    music_info = {}
    with open(file, 'r') as fp:
        line1 = fp.readline() # line: album, artist, year
        line1 = line1.strip().split(",")
        for line in fp:
            print(line)
        print(line1)

if __name__ == '__main__':
    print(music_data('music1.csv', 'rosie'))
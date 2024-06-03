import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

def main():
    url = input("Enter the URL you want to shorten: ")
    shortened_url = shorten_url(url)
    print("Shortened URL:", shortened_url)

if __name__ == "__main__":
    main()

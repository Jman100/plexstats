import requests, json, re
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyPHAT("black")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 12) #grandparent_title if media_type = episode
font2 = ImageFont.truetype(FredokaOne, 18)

r = requests.get("YOUR_API_URL")
f = open("tempfile.txt", "r")

data = json.loads(r.text)["response"]["data"]
stream_count = int(data["stream_count"])
emptyvar, height_addition = font.getsize("TEST")
height_addition = height_addition - 2
height_multiplier = 0
counter = 0


if f.read() != r.text.encode('ascii', 'ignore'):
        f.close()
        g = open("tempfile.txt", "w")
        g.write(r.text.encode('ascii', 'ignore'))
        g.close()
        if stream_count == 0:
                        message = "No Streams Active"
                        w, h = font2.getsize(message)
                        x = (inky_display.WIDTH / 2) - (w / 2)
                        y = (inky_display.HEIGHT / 2) - (h / 2)
                        draw.text((x, y), message, inky_display.BLACK, font2)
        else:

                        for session in data["sessions"]:
                                        if counter == 4:
                                                        remaining = str(int(stream_count) - counter)
                                                        message = "+ " + remaining + " more.."
                                                        w, h = font.getsize(message)
                                                        x = 0
                                                        y = inky_display.HEIGHT - height_addition
                                                        draw.text((x, y), message, inky_display.RED, font)
                                        else:
                                                        the_status = ""
                                                        the_title = ""
                                                        if session["state"] == "playing":
                                                                        the_status = "|>"
                                                        else:
                                                                        the_status = "| |"
                                                        if session["media_type"] == "episode":
                                                                        the_title = session["grandparent_title"]
                                                        else:
                                                                        the_title = session["title"]
                                                        message = the_title
                                                        w, h = font.getsize(message)
                                                        x = 0
                                                        y = height_addition * height_multiplier
                                                        draw.text((x, y), message, inky_display.RED, font)
                                                        height_multiplier = height_multiplier + 1

                                                        the_user = session["user"]
                                                        the_user = re.sub(r"@\S*", "", the_user)
                                                        message = "   " + the_user + " - " + session["progress_percent"] + "%  " + the_status   # progress_p$
                                                        w, h = font.getsize(message)
                                                        x = 0 #(inky_display.WIDTH / 2) - (w / 2)
                                                        y = height_addition * height_multiplier #(inky_display.HEIGHT / 2) - (h / 2)
                                                        draw.text((x, y), message, inky_display.BLACK, font)
                                                        height_multiplier = height_multiplier + 1
                                                        counter = counter + 1

                        message = str(int(data["total_bandwidth"]) / 1000) + " Mbps"
                        w, h = font.getsize(message)
                        x = inky_display.WIDTH - w
                        y = inky_display.HEIGHT - h
                        draw.text((x, y), message, inky_display.BLACK, font)

        inky_display.set_image(img)
        inky_display.show()


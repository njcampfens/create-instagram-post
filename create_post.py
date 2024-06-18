from html2image import Html2Image


available_slots = {
    0: '9:00, 10:00',
    1: '11:00, 12:00',
    2: '15:00, 19:00',
    3: '15:00',
    4: '9:00, 10:00, 11:00, 14:00'
}


hti = Html2Image()
hti.size = (1080, 1920)


with open('template.html', 'r') as html_file:
    html_content = html_file.read()

with open('template.css', 'r') as css_file:
    css_content = css_file.read()

html_content = html_content.replace('background.png', 
                                    '/Users/nestorjimenez/Desktop/my_repos/html_to_png/background.png')
html_content = html_content.format(available_slots[0], 
                                   available_slots[1], 
                                   available_slots[2], 
                                   available_slots[3], 
                                   available_slots[4] )

hti.screenshot(html_str=html_content, css_str=css_content, save_as='post.jpg')
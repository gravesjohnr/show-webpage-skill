from mycroft import MycroftSkill, intent_file_handler


class ShowWebpage(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('webpage.show.intent')
    def handle_webpage_show(self, message):
        self.speak_dialog('webpage.show')


def create_skill():
    return ShowWebpage()


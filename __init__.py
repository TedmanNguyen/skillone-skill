from mycroft import MycroftSkill, intent_file_handler


class Skillone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skillone.intent')
    def handle_skillone(self, message):
        self.speak_dialog('skillone')


def create_skill():
    return Skillone()


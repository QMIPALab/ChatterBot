from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import wikipedia


class WikipediaResponseAdapter(LogicAdapter):
    """
    Return a specific response to a specific input.

    :kwargs:
        * *input_text* (``str``) --
          The input text that triggers this logic adapter.
        * *output_text* (``str``) --
          The output text returned by this logic adapter.
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


#    def can_process(self, statement):
#        logic = ['what is', 'who is', 'what is a','siapa itu', 'siapa', 'siapakah','apa itu', 'apakah', 'kamu tau']
#        text = statement.text
#        try:
#            for i in logic:
#                if text.startswith(i):
#                    return True
#        except Exception as e:
#            print('this is your error')
#        return False

    def can_process(self, statement):
        logic = 'tolong search'
        text = statement.text
        try:
            if text.startswith(i):
                return True
        except Exception as e:
            print('error')
        return False

    def process(self, statement, additional_response_selection_parameters=None):
        #logic = ['what is', 'who is', 'what is a','siapa itu', 'siapa', 'siapakah','apa itu', 'apakah', 'kamu tau']
        logic = 'tolong search'
        text = statement.text
        idx=0
        try:
            for i in logic:
                if text.startswith(i):
                    l=int(len(logic[idx]))
                    break
                else:
                    idx+=1
        except Exception:
            print('no its here')
        request=statement.text[l:]
        try:
            if idx <= 2:
                wikipedia.set_lang('en')
                websum=wikipedia.summary(request, sentences=1)
                self.response_statement = Statement(text=websum)
                self.response_statement.confidence = 0.7
            else:
                wikipedia.set_lang('id')
                websum=wikipedia.summary(request, sentences=1)
                self.response_statement = Statement(text=websum)
                self.response_statement.confidence = 0.7
        except:
            if idx == 0 or idx == 2:
                self.response_statement = Statement(text='sorry, we dont know what that is')
            if idx == 1:
                self.response_statement = Statement(text='sorry, we dont know who that is')
            if idx > 2:
                self.response_statement = Statement(text='mohon maaf, saya tidak tahu')
            self.response_statement.confidence = 0.7
        return self.response_statement

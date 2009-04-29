#
# ui_controller_review.py <Peter.Bienstman@UGent.be>
#

from mnemosyne.libmnemosyne.component_manager import scheduler


class UiControllerReview(object):
    
    """Controls the behaviour of a widget which implements the ReviewWidget
    interface.
    
    """

    def __init__(self):
        self.widget = None
        self.card = None
        self.learning_ahead = False

    def reset(self):
        raise NotImplementedError

    def rollover(self):

        """To be called when a new day starts."""
        
        pass

    def new_question(self, learn_ahead=False):
        raise NotImplementedError    
        
    def show_answer(self):
        raise NotImplementedError

    def grade_answer(self, grade):
        raise NotImplementedError        

    def rebuild_queue(self):

        """Called when something in the GUI could have invalidated the queue.
        (e.g. card deletion).

        """

        sch = scheduler()
        sch.reset()
        sch.rebuild_queue()
        if not sch.in_queue(self.card):
            self.new_question()
        else:
            sch.remove_from_queue(self.card) 
        
    def update_dialog(self):
        raise NotImplementedError
  


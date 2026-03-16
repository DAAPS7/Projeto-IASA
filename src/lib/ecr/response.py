class Response:

    def __init__(self, action):
        self._action = action

    def activate(self, perception, intensity=0):
        """Retorna uma ação"""
        action = self._obtain_action(perception)
        
        if action is not None:
            action.priority(intensity)

        return action
    
    def _obtain_action(self, perception):
        """Por omissão retorna a ação do atributo"""
        return self._action
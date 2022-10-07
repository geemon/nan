class Jobs:
    def __init__(self, title, positon):
        self.title = title
        self.position = positon
    def describe_job(self):
        print(f'{self.title} is job name')
    
    def post(self):
        print(f'I am the {self.position}')
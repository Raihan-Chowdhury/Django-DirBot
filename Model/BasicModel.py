class Post(models.Model):
    #Fields
    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # Return Something (Helps to detect objects in admin)
    def __str__(self):
        return str(self.title)
    # To Avoid Error
    objects = models.Manager()
    # To Avoid Errors + ... 
    class Meta:
        # Ordering Datas
        ordering = ['-created']
        managed = True

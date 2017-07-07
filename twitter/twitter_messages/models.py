from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Message(models.Model):
    """Model definition for Message."""

    # TODO: Define fields here
    text = models.TextField(max_length=666)
    sender = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='messages_sent')
    receiver = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='messages_received')
    was_read = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Message."""

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    @property
    def message_text_short(self):
        # show first 20 characters of a message
        return self.text[:20]
    
    def __str__(self):
        return 'text: {text} from: {sender}, to: {receiver}, read: {was_read}'.format(
            text=self.message_text_short,
            sender=self.sender.username,
            receiver=self.receiver.username,
            was_read=self.was_read,
        )

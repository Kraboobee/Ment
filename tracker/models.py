"""Module contains journal and trackers.

The Journal will have one entry per day, and contain a to-do list
"""

from django.db                  import models
from django.contrib.auth.models import User
from django.core.validators     import MaxValueValidator, MinValueValidator
from users.models               import User, EnjoyMent, TreatMent, FulfilMent


class Entry(models.Model):
    """An Entry in the user's journal.
    
    There is one entry per day
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_entry')
    date = models.DateField(auto_now_add=True)
    # body = models.TextField(blank=True)
     
    class Meta:
        ordering            = ['-date']
        verbose_name_plural = "Entries"
        unique_together     = ('user', 'date')

    def __str__(self):
        return 'Entry on {}'.format(self.date)
    
    #TODO
        # autosave day's events at midnight
            # Info should be added to relevant database and filtered by date
            #Url for date should be ~ ment/user/date/mmddyyyy
        # show tasks in Entry
        # get absolute url
        

class Mood(models.Model):
    """Tracker for user's mood over time"""
    entry           = models.OneToOneField(Entry, on_delete=models.CASCADE)
    high_mood       = models.IntegerField(default=0,
                                          validators=[MaxValueValidator(5), MinValueValidator(0)])         # User's peak mood of the day - default 5/10 or 0 for BPD
    low_mood        = models.IntegerField(default=0,
                                          validators=[MaxValueValidator(5), MinValueValidator(0)])         # User's lowest mood of the day - see above
    notes           = models.CharField(max_length=140)       # Notes for the user's medical professionals to read
    
    def __str__(self):
        return '{} mood on {}'.format(self.entry.user.username, self.entry.date)
    
    
class CommitMent(models.Model):
    """A Task for the user to complete.
    
    There are many tasks per day
    """
    entry       = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='date_task')  # Date of task, to allow for tracking
    title       = models.CharField(max_length=100)                                              # Name of medication, hobby etc
    done        = models.BooleanField(default=False, blank=True, null=True)                     # If task has been completed today
    
    def __str__(self):
        return '{} on {}'.format(self.title, self.entry.date)
    

class Habit(models.Model):
    entry           = models.ForeignKey(Entry, on_delete=models.ForeignKey)
    habit           = models.ForeignKey(FulfilMent, 
                                        on_delete=models.CASCADE, 
                                        related_name='habit_on_date')       # Task appears on todo every day
    time_qty        = models.IntegerField(default=0)                        # Time or quantity spent or consumed                                   
    
    def __str__(self):
        return '{} Habit on {}'.format(self.entry.user.username, self.entry.date)
    
class MedTracker(models.Model):
    entry           = models.ForeignKey(Entry, 
                                        on_delete=models.CASCADE, 
                                        related_name='date_meds')
    dose            = models.ForeignKey(TreatMent,
                                        on_delete=models.CASCADE,
                                        related_name='meds_on_date')
    
    def __str__(self):
        return '{} Medication on {}'.format(self.entry.user.username, self.entry.date)
    
class Homework(CommitMent):
    due_date        = models.DateField()        # If medical professional gives homework. Reappears on next days Todo until done = True
    repeating       = models.BooleanField()     # If once-off or daily
    
    
#______________________________________________________________NOTES__________________________________________________________________#


    #TODO
        # Create():
            # if time = 00:00:
                # new MoodTracker
                
                # for FulfilMent in user.FulfilMents:
                    # new CommitMent(Entry = today, title = Fulfilment name)
                
                # for i in range (user.Medication.doses):
                    # new Commitment(title = "Medication.name" + "dose i")
                    
                # if yesterday's homework.done == False:
                    # new CommitMent()
            
        # getDifference(data, end_date, start_date)
        # lastIncrease/lastDecrease -> date of last increase/decrease


#TODO
    # Habits/Hobbies 
        # recommended: Sleep, eat, exercise, shower, speak to friends, drink, smoke, drugs
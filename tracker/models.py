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
    # slug
    body = models.TextField()
    # mood = models.IntegerField(default=5)

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
        # show tasks in Journal
        # get absolute url

    
class CommitMent(models.Model):
    """A Task for the user to complete.
    
    There are many tasks per day
    """
    entry   = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='date_task')  # Date of task, to allow for tracking
    title   = models.CharField(max_length=100)                                              # Name of medication, hobby etc
    done    = models.BooleanField(default=False, blank=True, null=True)                     # If task has been completed today
    
    def __str__(self):
        return '{} on {}'.format(self.title, self.entry.date)
    
    #TODO
        # getData                   -> return all info from given date. Possibly API
        # getDifference(data, end_date, start_date)
        # lastIncrease/lastDecrease -> date of last increase/decrease

# Perhaps some things will be required, some recommended, and some optional

#TODO
    # Mood Tracker
        # Check mood every day
        # Average is required
        
    # Homework Tracker
        # If done once, never refreshed

    # Different Tracker superclass
        # Subclasses for:
            # Medication
                # Each daily dose -> Task
                # Refreshes daily
            # Habits/Hobbies
                # Each habit -> Task
                # Refreshes daily
                # recommended: Sleep, eat, exercise, shower, speak to friends, drink, smoke, drugs


class MoodTracker(models.Model):
    """Tracker for user's mood over time"""
    date_recorded   = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='mood_on_date')
    ave_mood        = models.IntegerField(
                                default=5,
                                validators=[MaxValueValidator(10), MinValueValidator(1)] 
                                )
    high_mood       = models.IntegerField(default=5)         # User's peak mood of the day - default 5/10 or 0 for BPD
    low_mood        = models.IntegerField(default=5)         # User's lowest mood of the day - see above
    notes           = models.CharField(max_length=140)       # Notes for the user's medical professionals to read

#     # user.MoodHistory.ave_mood by default. User may input median/perceived average
#     # if user.hasBPD(): default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)]
#     # functions
#         # setAverage -> best + lowest / 2

# #     class Meta(Tracker.Meta):
# #         db_table = 'mood'

class HabitTracker(models.Model):
    date_recorded   = models.ForeignKey(Entry, on_delete=models.ForeignKey)
    name            = models.ForeignKey(FulfilMent, on_delete=models.CASCADE, related_name='habit_on_date')
    done            = models.BooleanField(default=False)
    time_spent      = models.IntegerField(default=0)
    
    
class MedTracker(models.Model):
    date_recorded   = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='meds_on_date')
    done            = models.BooleanField(default=False)

#______________________________________________________________NOTES__________________________________________________________________#


# class Tracker(models.Model):
#     """Abstract class from which all trackers will inherit"""
#     user        = models.ForeignKey(User, on_delete=models.CASCADE) # The user whose tracker this is
#     date        = models.DateField(auto_now_add=True)               # Should be unique. Only editable on date created  
#     done        = models.BooleanField(default=False)                # If a task has been completed today
#     time_spent  = models.IntegerField(blank=True, null=True)        # Time in minutes - Used for Hobbies/Habits if > 0, done = True

#     class Meta:
#         abstract = True
#         ordering = ['-date']
        

                   
        

# # Tracks user's habits and hobbies. Can be good or bad. User can measure time spent or quantity (Cigarettes/drinks)
# class HabitTracker(Tracker):
#     pass
    

#     # class Meta(Tracker.Meta):
#     #     db_table = 'habits'
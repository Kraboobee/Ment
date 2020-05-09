"""user model for profile information.

This module will contain the information for the user, including contact
information and demographic information
"""

from django.db                  import models
from django.contrib.auth.models import User

# TODO
    # API for USER
        # name
        # medication name and number of doses for each medication
        # habit name for each habit
        # average mood -> maybe. The default might just be deviation of 0

class Profile(models.Model):
    """User's Profile"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return '{} Profile'.format(self.user.username)

    
THERAPIST       = 'Therapist'
PSYCHIATRIST    = 'Psychiatrist'
DOCTOR          = 'Doctor'
FAMILY          = 'Family'
FRIEND          = 'Friend'

CATEGORY_CHOICES = [
    (THERAPIST,     'Therapist'),
    (PSYCHIATRIST,  'Psychiatrist'),
    (DOCTOR,        'Doctor'),
    (FAMILY,        'Family'),
    (FRIEND,        'Friend'),
    ('',            'Any')
]
class AccompaniMent(models.Model):
    """Contact information for important people in the user's life"""
    name = models.CharField(max_length=50)
    role = models.CharField(
        max_length  = 12,
        choices     = CATEGORY_CHOICES,
        default     = FRIEND,
    )
    tel_no = models.CharField(max_length=20, blank=True, null=True)
    tel_no2 = models.CharField(max_length=20, blank=True, null=True)
    tel_no3 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return 'Contact details for {} ({})'.format(self.name, self.role)


class EnjoyMent(models.Model):
    """The user's mood history"""
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    ave_mood        = models.IntegerField(default=5)    # average mood of all time
    lowest_mood     = models.IntegerField(default=5)    # if date.low_mood < lowest_mood: lowest_mood = date.low_mood
    highest_mood    = models.IntegerField(default=5)    # see above
    
    def __str__(self):
        return '{} Mood History'.format(self.user.username)

    
class TreatMent(models.Model):
    """The user's prescribed medication"""
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    name                = models.CharField(max_length=25)                        # Name of medication
    prescribed_dosage   = models.IntegerField()                     # Prescribed dosage per pill - default mg
    # g or mg                                                       # if dosage in mg or g
    doses_per_day       = models.IntegerField()                     # To track if user has taken all required doses
    pills_remaining     = models.IntegerField()                     # Notify user when this is < (7 * doses_per_day) to allow a week to refill
    scriptRepeats       = models.IntegerField(default=0)            # default and min 0; if > 0, scriptAvail = True; --1 after refill 
    scriptAvail         = models.BooleanField(default=False)        # if meds running out, tell user to get new script
    start_date          = models.DateField(null=True, blank=True)
    end_date            = models.DateField(null=True, blank=True)
    active              = models.BooleanField(default=True)         # if user is currently on this medication

    # functions
    def __str__(self):
        return '{} Medication ({} {})'.format(self.user.username, self.name, self.prescribed_dosage)
    
    def refill(self, num_pills=30):
        """Method to increase count of pills after collection. Default 30 pills"""
        self.pills_remaining += num_pills
        return 'You now have {} pills remaining'.format(self.pills_remaining)
    
    def refill_notify(self):
        """Notifies user that their medication supply is running low"""
        return 'You currently have {} {} pills left. You should go to the pharmacy soon.'.format(self.pills_remaining, self.name)
    
    def renew_notify(self):
        """Notifies user that they need a new prescription"""
        return 'You do not have a prescription to collect your medication. You should speak to your doctor.'
        
    def take_meds(self):
        """Reduces pills remaining when user takes their dose"""
        self.pills_remaining -= 1
        
        if self.pills_remaining == 0:
            renew_notify()
            
        if self.pills_remaining <= (7 * self.doses_per_day):
            refill_notify()
                
            
    def renew_script(self, num_repeats=1):
        """Method to renew prescription. Default 1 repeat"""
        self.scriptRepeats += num_repeats
        self.scriptAvail    = True
            
        # update script  -> change medication or qty -> set end date of current script, and create new object
        # take meds      -> reduce pills remaining when user has taken pills 
            # Error handling required to ensure user takes all doses on time
            # Maybe one tracker per name    
            
# Choices for Habit model
HABIT = 'Habit'
HOBBY = 'Hobby'

CATEGORY_CHOICES = [
    (HABIT, 'Habit'),
    (HOBBY, 'Hobby'),
    ('', 'Any'),
]

class FulfilMent(models.Model):
    """A habit or hobby the user is trying to keep up with"""
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    name                = models.CharField(max_length=25)
    category            = models.CharField(
                              max_length  = 5,
                              choices     = CATEGORY_CHOICES,
                              default     = HABIT
                          )
    is_good             = models.BooleanField(default=True)
    goal_time_qty       = models.IntegerField(null=True, blank=True)    # Goal time or quantity
    total_time_qty      = models.IntegerField(default=0)                # Total amount of time the user has spent on his or her hobby/habit
    
    def __str__(self):
        return '{} {}: {}'.format(self.user.username, self.category, self.name)
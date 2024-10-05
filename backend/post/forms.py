from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Post, PostAttachment, Event, EventAttachment,EventRegistration
import re

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 
            'description', 
            'contact_information', 
            'price', 
            'category', 
            'breed', 
            'color', 
            'age', 
            'vaccinated', 
            'gender', 
            'weight', 
            'microchipped', 
            'trained', 
            'health_certificate', 
            'body'
        ]
        help_texts = {
            'age': 'Age in months',
            'weight': 'Weight in kilograms',
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Price must be a positive number.")
        return price

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 0:
            raise ValidationError("Age cannot be negative.")
        return age

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight <= 0:
            raise ValidationError("Weight must be a positive number.")
        return weight


class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # Limit file size to 5MB
                raise ValidationError("Image file too large ( > 5MB ).")
        return image


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']    


class EventAttachmentForm(ModelForm):
    class Meta:
        model = EventAttachment
        fields = ['image']  

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # Limit file size to 5MB
                raise ValidationError("Image file too large ( > 5MB ).")
        return image

class EventRegistrationForm(ModelForm):
    class Meta:
        model = EventRegistration
        fields = [
            'full_name', 
            'email', 
            'contact', 
            'address', 
            'selected_event', 
            'pet_type', 
            'pet_name', 
            'pet_dob', 
            'vaccination_card', 
            'agree_to_terms'
        ]

    def clean(self):
        cleaned_data = super().clean()
        pet_type = cleaned_data.get('pet_type')
        pet_name = cleaned_data.get('pet_name')
        pet_dob = cleaned_data.get('pet_dob')
        vaccination_card = cleaned_data.get('vaccination_card')

        # Validate pet fields if a pet type is provided
        if pet_type and pet_type.lower() != 'none':  # Assuming 'none' is the option for no pet
            if not pet_name:
                self.add_error('pet_name', "Pet name is required if pet type is selected.")
            if not pet_dob:
                self.add_error('pet_dob', "Pet date of birth is required if pet type is selected.")
            if not vaccination_card:
                self.add_error('vaccination_card', "Vaccination card is required if pet type is selected.")

    def clean_vaccination_card(self):
        vaccination_card = self.cleaned_data.get('vaccination_card')
        if vaccination_card:
            if vaccination_card.size > 5 * 1024 * 1024:  # Limit file size to 5MB
                raise ValidationError("File too large ( > 5MB ).")
        return vaccination_card
    
    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        phone_pattern = r'^\+?1?\d{9,15}$'  # Simple regex for phone numbers
        if not re.match(phone_pattern, contact):
            raise ValidationError("Enter a valid contact number.")
        return contact
    
    def clean_agree_to_terms(self):
        agree = self.cleaned_data.get('agree_to_terms')
        if not agree:
            raise ValidationError("You must agree to the terms and conditions.")
        return agree

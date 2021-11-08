from rest_framework import fields, serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .models import FollowingVenues, Venue, Band, FollowingBands


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "postal_code",
            "is_band",
            "is_venue",
        )

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            postal_code=validated_data["postal_code"],
            is_band=validated_data["is_band"],
            is_venue=validated_data["is_venue"]
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ["id", "user_id", "band_name", "song_to_display"]


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ["id", "user_id", "venue_name", "address"]


class FollowingBandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowingBands
        fields = ["id", "user_id", "band_id"]


class FollowingVenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowingVenues
        fields = ["id", "user_id", "venue_id"]

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .models import Schedule, Venue, Band, FollowingBands, FollowingVenues, User
from .serializers import (
    RegistrationSerializer,
    BandSerializer,
    ScheduleSerializer,
    VenueSerializer,
    FollowingVenuesSerializer,
    FollowingBandsSerializer,
)


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_band(request):
    if request.method == "POST":
        request.user
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_venue(request):
    if request.method == "POST":
        request.user
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    print(user_id)
    user = User.objects.get(id=user_id)
    serializer = RegistrationSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_bands(request):
    bands = Band.objects.all()
    serializer = BandSerializer(bands, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_venues(request):
    venues = Venue.objects.all()
    serializer = VenueSerializer(venues, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_band_follow(request):
    if request.method == "POST":
        request.user
        serializer = FollowingBandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_venue_follow(request):
    if request.method == "POST":
        request.user
        serializer = FollowingVenuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_followed_bands(request, user_id):

    bands = []
    followedBands = []
    followedBands = FollowingBands.objects.filter(user_id=user_id)

    for fband in followedBands:
        bandId = fband.band_id_id
        band = Band.objects.get(id=bandId)
        bands.append(band)

    serializer = BandSerializer(bands, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_followed_venues(request, user_id):

    venues = []
    followedVenues = []
    followedVenues = FollowingVenues.objects.filter(user_id=user_id)

    for fvenue in followedVenues:
        venueId = fvenue.venue_id_id
        venue = Venue.objects.get(id=venueId)
        venues.append(venue)

    serializer = VenueSerializer(venues, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def make_show_date(request):
    if request.method == "POST":
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_schedule(request):

    schedule = Schedule.objects.all()
    serializer = ScheduleSerializer(schedule, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_logged_in_band(request, id):
    band = Band.objects.get(user_id=id)
    serializer = BandSerializer(band)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_logged_in_venue(request, id):
    venue = Venue.objects.get(user_id=id)
    serializer = VenueSerializer(venue)
    return Response(serializer.data)

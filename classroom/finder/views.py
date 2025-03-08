from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Room, Feedback

def home(request):
    selected_block = request.GET.get('block', '')  
    rooms = Room.objects.filter(block=selected_block) if selected_block else Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms, 'selected_block': selected_block})

def post_room(request):
    if request.method == "POST":
        block = request.POST.get('block')
        room_number = request.POST.get('room_number')

        if block and room_number:
            # Ensure the room doesn't already exist before creating it
            if not Room.objects.filter(block=block, room_number=room_number).exists():
                Room.objects.create(block=block, room_number=room_number)
                messages.success(request, f"Room {room_number} in Block {block} added successfully!")
            else:
                messages.error(request, f"Room {room_number} in Block {block} already exists!")

        return redirect('home')  

    return render(request, 'home.html')

def remove_room(request):
    if request.method == "POST":
        block = request.POST.get("block")
        room_number = request.POST.get("room_number")

        try:
            room = Room.objects.get(block=block, room_number=room_number)
            room.delete()
            messages.success(request, f"Room {room_number} in Block {block} removed successfully!")
        except Room.DoesNotExist:
            messages.error(request, "Room not found!")

        return redirect("home")  

    return render(request, "home.html")


def feedback_view(request):
    if request.method == "POST":
        message = request.POST.get("message", "").strip()

        if not message:
            messages.error(request, "Message cannot be empty!")
        else:
            Feedback.objects.create(message=message)
            messages.success(request, "Thank you for your feedback!")

        return redirect("home")  # Redirect to the home page

    return redirect("home")  # Redirect if accessed via GET


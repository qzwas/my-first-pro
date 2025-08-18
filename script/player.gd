extends KinematicBody2D
#i said
const SPEED = 100.0
const JUMP_VELOCITY = -250.0
const GRAVITY = 980.0

var velocity = Vector2()

func _physics_process(delta):
	# Add the gravity FIRST
	if not is_on_floor():
		velocity.y += GRAVITY * delta

	# Handle jump - test both methods
	if Input.is_key_pressed(KEY_SPACE):
		
		if is_on_floor():
			velocity.y = JUMP_VELOCITY
			
	# Get the input direction using direct key input
	var direction = 0
	if Input.is_key_pressed(KEY_RIGHT):
		direction += 1
		
	if Input.is_key_pressed(KEY_LEFT):
		direction -= 1
	if direction != 0:
		velocity.x = direction * SPEED
	else:
		velocity.x = lerp(velocity.x, 0, 0.1)

	# Move the character
	velocity = move_and_slide(velocity, Vector2.UP)


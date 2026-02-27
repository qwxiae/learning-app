### Stepik.org
<!-- Basics -->
https://stepik.org/
https://stepik.org/catalog
https://stepik.org/teach/courses/new
https://stepik.org/catalog?auth=login
https://stepik.org/catalog?auth=registration
https://stepik.org/users/483341705


https://stepik.org/learn?auth=login&pass_reset=true
https://stepik.org/catalog?show_catalog=true
https://stepik.org/catalog?show_catalog=c4
https://stepik.org/catalog/400

https://stepik.org/course/232766/promo?search=8851132375
https://stepik.org/catalog/search?cert=true&free=true&q=ddas

<!-- Enrolled / My Courses -->
https://stepik.org/learn
https://stepik.org/learn/courses
https://stepik.org/notifications?type=learn


https://stepik.org/edit-profile/notifications
https://stepik.org/edit-profile/email
<!-- Edit profile -->
https://stepik.org/edit-profile/info
https://stepik.org/edit-profile/oauth


https://stepik.org/users/637368430/profile
https://stepik.org/users/637368430/certificates


<!-- Create Course -->
https://stepik.org/teach/courses/new
https://stepik.org/course/275962/edit
https://stepik.org/edit-lesson/2238910/step/1


## Auth 
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/password-reset
POST /api/v1/auth/password-confirm
POST /api/v1/auth/verify-email
POST /api/v1/auth/refresh

## Users
GET /api/v1/users/{id}
GET /api/v1/users/{id}/certificates
### My profile
GET   /api/v1/users/me
PATCH /api/v1/users/me

## Catalog
GET /api/v1/courses
    ?search=python
    ?free=true
    ?certificate=true
    ?level=beginner
    ?ordering=popular

## Course
GET /api/v1/courses/{course_id}
GET /api/v1/courses/{course_id}/certificate

## Enrollment
POST /api/v1/courses/{course_id}/enroll
GET /api/v1/enrollments/my
GET /api/v1/enrollments/{enrollment_id}

## Modules
GET /api/v1/courses/{course_id}/modules
GET /api/v1/courses/{course_id}/modules/{module_id}

## Lessons
GET /api/v1/courses/{course_id}/modules/{module_id}/lessons
GET /api/v1/courses/{course_id}/modules/{module_id}/lessons/{lesson_id}

#### Theory
```json
{
    "id": 10,
  "type": "theory",
  "content": "<html>...</html>"
}
```
#### Single Choice
```json
{
  "id": 12,
  "type": "single_choice",
  "question": "What is 2+2?",
  "options": [
    {"id": 1, "text": "3"},
    {"id": 2, "text": "4"}
  ]
}
```

#### Text Input
```json
{
  "id": 14,
  "type": "text_input",
  "question": "Define polymorphism"
}
```

### Code
```json
{
  "id": 16,
  "type": "code",
  "description": "Write a function sum(a, b)",
  "constraints": "1 ≤ a,b ≤ 10^9"
}
```
## Attempts
<!-- Hisotory of attempts -->
POST /courses/{c}/modules/{m}/lessons/{l}/attempts
GET  /courses/{c}/modules/{m}/lessons/{l}/attempts/{attempt_id}
POST /courses/{c}/modules/{m}/lessons/{l}/attempts/{attempt_id}

### Choice
```json
{
  "selected_option_id": 2
}
```
### Text
```json
{
  "text_answer": "Polymorphism is..."
}
```
### Code
```json
{
  "code_answer": "def sum(a,b): return a+b"
}
```
```json
{
  "is_correct": true,
  "score": 1,
  "status": "completed",
  "lesson_completed": true
}
```
## Notifications
GET   /api/v1/notifications
PATCH /api/v1/notifications/{id}

## Teach
/api/v1/teach/
POST /api/v1/teach/courses
PATCH /api/v1/teach/courses/{course_id}
POST /api/v1/teach/courses/{course_id}/modules
POST /api/v1/teach/courses/{course_id}/modules/{module_id}/lessons
```json
{
  "title": "Variables",
  "type": "single_choice"
}
```
<!-- Варианты для single choice -->
POST /api/v1/teach/lessons/{lesson_id}/options
<!-- Add lesson content -->
PATCH /api/v1/teach/lessons/{lesson_id}

Catalog → Course → Enroll → Module → Lesson → Attempt → Result → Certificate

Catalog → Course → Enroll → Module → Lesson → Attempt → Result → Certificate



```yaml
openapi: 3.0.3
info:
  title: Stepik-like LMS API
  version: 1.0.0
  description: Simplified LMS inspired by Stepik

servers:
  - url: /api/v1

tags:
  - name: Auth
  - name: Users
  - name: Courses
  - name: Enrollments
  - name: Modules
  - name: Lessons
  - name: Attempts
  - name: Notifications
  - name: Certificates
  - name: Teach

paths:

  # ================= AUTH =================

  /auth/register:
    post:
      tags: [Auth]
      summary: Register user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RegisterRequest'
      responses:
        '201':
          description: Created

  /auth/login:
    post:
      tags: [Auth]
      summary: Login
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoginRequest'
      responses:
        '200':
          description: JWT tokens returned

  # ================= USERS =================

  /users/{user_id}:
    get:
      tags: [Users]
      summary: Public profile
      parameters:
        - $ref: '#/components/parameters/UserId'
      responses:
        '200':
          description: User profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

  /users/me:
    get:
      tags: [Users]
      summary: Current user
      responses:
        '200':
          description: Current user
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
    patch:
      tags: [Users]
      summary: Update profile
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserUpdate'

  # ================= COURSES =================

  /courses:
    get:
      tags: [Courses]
      summary: List courses
      parameters:
        - in: query
          name: search
          schema:
            type: string
        - in: query
          name: level
          schema:
            type: string
      responses:
        '200':
          description: List of courses
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Course'

  /courses/{course_id}:
    get:
      tags: [Courses]
      summary: Course details
      parameters:
        - $ref: '#/components/parameters/CourseId'
      responses:
        '200':
          description: Course details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CourseDetail'

  /courses/{course_id}/enroll:
    post:
      tags: [Enrollments]
      summary: Enroll in course
      parameters:
        - $ref: '#/components/parameters/CourseId'
      responses:
        '201':
          description: Enrolled

  # ================= MODULES =================

  /courses/{course_id}/modules:
    get:
      tags: [Modules]
      summary: List modules
      parameters:
        - $ref: '#/components/parameters/CourseId'
      responses:
        '200':
          description: Modules list
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Module'

  # ================= LESSONS =================

  /courses/{course_id}/modules/{module_id}/lessons:
    get:
      tags: [Lessons]
      summary: List lessons
      parameters:
        - $ref: '#/components/parameters/CourseId'
        - $ref: '#/components/parameters/ModuleId'
      responses:
        '200':
          description: Lessons list
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Lesson'

  /courses/{course_id}/modules/{module_id}/lessons/{lesson_id}:
    get:
      tags: [Lessons]
      summary: Lesson detail
      parameters:
        - $ref: '#/components/parameters/CourseId'
        - $ref: '#/components/parameters/ModuleId'
        - $ref: '#/components/parameters/LessonId'
      responses:
        '200':
          description: Lesson detail
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LessonDetail'

  # ================= ATTEMPTS =================

  /courses/{course_id}/modules/{module_id}/lessons/{lesson_id}/attempts:
    post:
      tags: [Attempts]
      summary: Start attempt
      parameters:
        - $ref: '#/components/parameters/CourseId'
        - $ref: '#/components/parameters/ModuleId'
        - $ref: '#/components/parameters/LessonId'
      responses:
        '201':
          description: Attempt created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Attempt'

  /courses/{course_id}/modules/{module_id}/lessons/{lesson_id}/attempts/{attempt_id}:
    post:
      tags: [Attempts]
      summary: Submit answer (auto-complete)
      parameters:
        - $ref: '#/components/parameters/CourseId'
        - $ref: '#/components/parameters/ModuleId'
        - $ref: '#/components/parameters/LessonId'
        - $ref: '#/components/parameters/AttemptId'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnswerRequest'
      responses:
        '200':
          description: Result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AttemptResult'

components:

  parameters:
    UserId:
      name: user_id
      in: path
      required: true
      schema:
        type: integer
    CourseId:
      name: course_id
      in: path
      required: true
      schema:
        type: integer
    ModuleId:
      name: module_id
      in: path
      required: true
      schema:
        type: integer
    LessonId:
      name: lesson_id
      in: path
      required: true
      schema:
        type: integer
    AttemptId:
      name: attempt_id
      in: path
      required: true
      schema:
        type: integer

  schemas:

    RegisterRequest:
      type: object
      required: [email, password]
      properties:
        email:
          type: string
        password:
          type: string

    LoginRequest:
      type: object
      required: [email, password]
      properties:
        email:
          type: string
        password:
          type: string

    User:
      type: object
      properties:
        id:
          type: integer
        username:
          type: string
        bio:
          type: string

    UserUpdate:
      type: object
      properties:
        bio:
          type: string

    Course:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        level:
          type: string

    CourseDetail:
      allOf:
        - $ref: '#/components/schemas/Course'
        - type: object
          properties:
            description:
              type: string
            modules_count:
              type: integer

    Module:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        order:
          type: integer

    Lesson:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        type:
          type: string
          enum: [theory, single_choice, text_input, code]

    LessonDetail:
      allOf:
        - $ref: '#/components/schemas/Lesson'
        - type: object
          properties:
            content:
              type: string

    Attempt:
      type: object
      properties:
        id:
          type: integer
        status:
          type: string

    AnswerRequest:
      type: object
      properties:
        selected_option_id:
          type: integer
        text_answer:
          type: string
        code_answer:
          type: string

    AttemptResult:
      type: object
      properties:
        is_correct:
          type: boolean
        score:
          type: number
        status:
          type: string
```

```yaml
openapi: 3.0.3
info:
  title: Stepik-like Educational Platform API
  description: |
    REST API for an online educational platform inspired by Stepik.org.
    Supports course catalog browsing, enrollment, lesson management,
    user profiles, certificates, and notifications.
  version: 1.0.0
  contact:
    name: API Support
    email: api@platform.example.com

servers:
  - url: https://api.platform.example.com/v1
    description: Production server
  - url: http://localhost:8000/api/v1
    description: Local development server

tags:
  - name: Auth
    description: Registration, login, and password management
  - name: Catalog
    description: Course catalog and search
  - name: Courses
    description: Course details and enrollment
  - name: Lessons
    description: Lesson content and steps
  - name: Users
    description: User profiles and certificates
  - name: Profile
    description: Editing the authenticated user's profile
  - name: Notifications
    description: User notifications
  - name: Teaching
    description: Course authoring and management

# ─────────────────────────────────────────────
# SECURITY
# ─────────────────────────────────────────────
security:
  - bearerAuth: []

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  # ───── REUSABLE SCHEMAS ─────
  schemas:

    # --- Auth ---
    RegisterRequest:
      type: object
      required: [email, password, first_name, last_name]
      properties:
        email:
          type: string
          format: email
          example: student@example.com
        password:
          type: string
          format: password
          minLength: 8
          example: SecurePass123
        first_name:
          type: string
          example: Ivan
        last_name:
          type: string
          example: Petrov

    LoginRequest:
      type: object
      required: [email, password]
      properties:
        email:
          type: string
          format: email
          example: student@example.com
        password:
          type: string
          format: password
          example: SecurePass123

    TokenResponse:
      type: object
      properties:
        access_token:
          type: string
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        refresh_token:
          type: string
          example: dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...
        token_type:
          type: string
          example: bearer
        expires_in:
          type: integer
          description: Seconds until access token expires
          example: 3600

    PasswordResetRequest:
      type: object
      required: [email]
      properties:
        email:
          type: string
          format: email
          example: student@example.com

    PasswordResetConfirm:
      type: object
      required: [token, new_password]
      properties:
        token:
          type: string
          example: abc123resettoken
        new_password:
          type: string
          format: password
          minLength: 8
          example: NewSecurePass456

    # --- Users ---
    UserProfile:
      type: object
      properties:
        id:
          type: integer
          example: 483341705
        first_name:
          type: string
          example: Ivan
        last_name:
          type: string
          example: Petrov
        bio:
          type: string
          nullable: true
          example: Python developer and lifelong learner.
        avatar_url:
          type: string
          format: uri
          nullable: true
          example: https://cdn.platform.example.com/avatars/483341705.jpg
        joined_at:
          type: string
          format: date-time
          example: "2023-01-15T10:00:00Z"
        courses_completed:
          type: integer
          example: 5

    Certificate:
      type: object
      properties:
        id:
          type: integer
          example: 1001
        course_id:
          type: integer
          example: 232766
        course_title:
          type: string
          example: Python for Beginners
        issued_at:
          type: string
          format: date-time
          example: "2024-06-01T12:00:00Z"
        certificate_url:
          type: string
          format: uri
          example: https://cdn.platform.example.com/certs/1001.pdf
        grade:
          type: number
          format: float
          minimum: 0
          maximum: 100
          example: 87.5

    # --- Profile ---
    ProfileUpdateRequest:
      type: object
      properties:
        first_name:
          type: string
          example: Ivan
        last_name:
          type: string
          example: Petrov
        bio:
          type: string
          example: Python developer and lifelong learner.
        avatar_url:
          type: string
          format: uri
          example: https://cdn.platform.example.com/avatars/me.jpg

    EmailUpdateRequest:
      type: object
      required: [email, current_password]
      properties:
        email:
          type: string
          format: email
          example: new_email@example.com
        current_password:
          type: string
          format: password
          example: CurrentPass123

    NotificationPreferences:
      type: object
      properties:
        email_on_comment:
          type: boolean
          example: true
        email_on_course_update:
          type: boolean
          example: true
        email_on_new_lesson:
          type: boolean
          example: false
        push_enabled:
          type: boolean
          example: true

    OAuthConnection:
      type: object
      properties:
        provider:
          type: string
          enum: [google, github, vk]
          example: google
        connected:
          type: boolean
          example: true
        connected_at:
          type: string
          format: date-time
          nullable: true
          example: "2024-01-10T08:30:00Z"
        email:
          type: string
          format: email
          nullable: true
          example: student@gmail.com

    # --- Catalog / Courses ---
    CourseShort:
      type: object
      properties:
        id:
          type: integer
          example: 232766
        title:
          type: string
          example: Python for Beginners
        slug:
          type: string
          example: python-for-beginners
        cover_url:
          type: string
          format: uri
          nullable: true
          example: https://cdn.platform.example.com/covers/232766.jpg
        author:
          $ref: '#/components/schemas/UserProfile'
        rating:
          type: number
          format: float
          minimum: 0
          maximum: 5
          example: 4.8
        enrolled_count:
          type: integer
          example: 15200
        is_free:
          type: boolean
          example: true
        has_certificate:
          type: boolean
          example: true
        category_id:
          type: integer
          nullable: true
          example: 4
        language:
          type: string
          example: ru

    CourseDetail:
      allOf:
        - $ref: '#/components/schemas/CourseShort'
        - type: object
          properties:
            description:
              type: string
              example: A comprehensive introduction to Python programming.
            requirements:
              type: string
              nullable: true
              example: Basic computer skills
            target_audience:
              type: string
              nullable: true
              example: Beginners with no prior coding experience
            modules:
              type: array
              items:
                $ref: '#/components/schemas/Module'
            created_at:
              type: string
              format: date-time
              example: "2022-09-01T00:00:00Z"
            updated_at:
              type: string
              format: date-time
              example: "2024-03-15T10:00:00Z"

    Category:
      type: object
      properties:
        id:
          type: integer
          example: 4
        name:
          type: string
          example: Programming
        slug:
          type: string
          example: programming
        courses_count:
          type: integer
          example: 340

    # --- Modules / Lessons / Steps ---
    Module:
      type: object
      properties:
        id:
          type: integer
          example: 10
        title:
          type: string
          example: Getting Started
        position:
          type: integer
          example: 1
        lessons:
          type: array
          items:
            $ref: '#/components/schemas/LessonShort'

    LessonShort:
      type: object
      properties:
        id:
          type: integer
          example: 2238910
        title:
          type: string
          example: Introduction to Variables
        position:
          type: integer
          example: 1
        steps_count:
          type: integer
          example: 5
        is_completed:
          type: boolean
          nullable: true
          description: Null if user is not enrolled
          example: false

    LessonDetail:
      allOf:
        - $ref: '#/components/schemas/LessonShort'
        - type: object
          properties:
            steps:
              type: array
              items:
                $ref: '#/components/schemas/Step'

    Step:
      type: object
      properties:
        id:
          type: integer
          example: 1
        position:
          type: integer
          example: 1
        type:
          type: string
          enum: [text, video, quiz, code, matching, fill_blank]
          example: text
        is_completed:
          type: boolean
          nullable: true
          example: false
        content:
          $ref: '#/components/schemas/StepContent'

    StepContent:
      type: object
      description: >
        Content varies by step type. For `text` — HTML body.
        For `quiz` — list of options. For `code` — problem statement + language.
      properties:
        html_body:
          type: string
          nullable: true
          example: "<p>In Python, a variable is a named storage location...</p>"
        video_url:
          type: string
          format: uri
          nullable: true
          example: https://cdn.platform.example.com/videos/step1.mp4
        options:
          type: array
          nullable: true
          description: For quiz steps
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              text:
                type: string
                example: "x = 5"
        problem_statement:
          type: string
          nullable: true
          example: Write a function that returns the sum of two numbers.
        language:
          type: string
          nullable: true
          enum: [python, javascript, sql, java, cpp]
          example: python

    StepSubmission:
      type: object
      required: [step_id, answer]
      properties:
        step_id:
          type: integer
          example: 1
        answer:
          description: >
            For quiz: array of selected option IDs.
            For code: source code string.
            For fill_blank / text: string answer.
          example: [2]

    SubmissionResult:
      type: object
      properties:
        submission_id:
          type: integer
          example: 99001
        step_id:
          type: integer
          example: 1
        status:
          type: string
          enum: [correct, wrong, pending]
          example: correct
        score:
          type: number
          format: float
          nullable: true
          example: 1.0
        feedback:
          type: string
          nullable: true
          example: "Well done!"
        submitted_at:
          type: string
          format: date-time
          example: "2024-06-01T09:00:00Z"

    # --- Enrollment ---
    Enrollment:
      type: object
      properties:
        id:
          type: integer
          example: 500
        course_id:
          type: integer
          example: 232766
        enrolled_at:
          type: string
          format: date-time
          example: "2024-01-20T14:00:00Z"
        progress_percent:
          type: number
          format: float
          minimum: 0
          maximum: 100
          example: 42.5
        last_active_at:
          type: string
          format: date-time
          nullable: true
          example: "2024-06-10T08:00:00Z"

    # --- Notifications ---
    Notification:
      type: object
      properties:
        id:
          type: integer
          example: 7001
        type:
          type: string
          enum: [comment_reply, course_update, new_lesson, achievement, system]
          example: course_update
        message:
          type: string
          example: "New lesson added to Python for Beginners!"
        is_read:
          type: boolean
          example: false
        created_at:
          type: string
          format: date-time
          example: "2024-06-12T10:00:00Z"
        link:
          type: string
          format: uri
          nullable: true
          example: https://platform.example.com/course/232766

    # --- Teaching / Course Editing ---
    CourseCreateRequest:
      type: object
      required: [title]
      properties:
        title:
          type: string
          example: My New Course
        description:
          type: string
          nullable: true
          example: An in-depth course on advanced topics.
        is_free:
          type: boolean
          example: true
        category_id:
          type: integer
          nullable: true
          example: 4
        language:
          type: string
          example: ru

    CourseUpdateRequest:
      type: object
      properties:
        title:
          type: string
          example: My Updated Course Title
        description:
          type: string
          example: Updated description.
        is_free:
          type: boolean
          example: false
        category_id:
          type: integer
          nullable: true
          example: 4
        language:
          type: string
          example: en

    LessonCreateRequest:
      type: object
      required: [title, module_id]
      properties:
        title:
          type: string
          example: Introduction to Lists
        module_id:
          type: integer
          example: 10
        position:
          type: integer
          example: 2

    StepCreateRequest:
      type: object
      required: [type, lesson_id]
      properties:
        lesson_id:
          type: integer
          example: 2238910
        type:
          type: string
          enum: [text, video, quiz, code, matching, fill_blank]
          example: quiz
        position:
          type: integer
          example: 1
        content:
          $ref: '#/components/schemas/StepContent'

    # --- Pagination ---
    PaginationMeta:
      type: object
      properties:
        total:
          type: integer
          example: 1240
        page:
          type: integer
          example: 1
        per_page:
          type: integer
          example: 20
        total_pages:
          type: integer
          example: 62

    # --- Errors ---
    Error:
      type: object
      properties:
        error:
          type: string
          example: not_found
        message:
          type: string
          example: The requested resource was not found.
        details:
          type: object
          nullable: true
          additionalProperties: true

  # ───── REUSABLE RESPONSES ─────
  responses:
    Unauthorized:
      description: Authentication credentials missing or invalid
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: unauthorized
            message: Authentication token is missing or expired.
    Forbidden:
      description: Insufficient permissions
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    ValidationError:
      description: Request validation failed
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: validation_error
            message: Input validation failed.
            details:
              email: ["This field is required."]

  # ───── REUSABLE PARAMETERS ─────
  parameters:
    PageParam:
      in: query
      name: page
      schema:
        type: integer
        default: 1
        minimum: 1
      description: Page number
    PerPageParam:
      in: query
      name: per_page
      schema:
        type: integer
        default: 20
        minimum: 1
        maximum: 100
      description: Results per page


# ─────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────
paths:

  # ══════════ AUTH ══════════

  /auth/register:
    post:
      tags: [Auth]
      summary: Register a new user
      description: Creates a new student account.
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RegisterRequest'
      responses:
        '201':
          description: Account created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenResponse'
        '400':
          $ref: '#/components/responses/ValidationError'
        '409':
          description: Email already registered
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /auth/login:
    post:
      tags: [Auth]
      summary: Log in with email and password
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoginRequest'
      responses:
        '200':
          description: Login successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenResponse'
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          description: Invalid credentials
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /auth/logout:
    post:
      tags: [Auth]
      summary: Log out (invalidate refresh token)
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [refresh_token]
              properties:
                refresh_token:
                  type: string
      responses:
        '204':
          description: Logged out successfully
        '401':
          $ref: '#/components/responses/Unauthorized'

  /auth/token/refresh:
    post:
      tags: [Auth]
      summary: Refresh access token
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [refresh_token]
              properties:
                refresh_token:
                  type: string
      responses:
        '200':
          description: New access token issued
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenResponse'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /auth/password-reset:
    post:
      tags: [Auth]
      summary: Request a password reset email
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PasswordResetRequest'
      responses:
        '200':
          description: Reset email sent if account exists
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: If this email is registered, a reset link has been sent.

  /auth/password-reset/confirm:
    post:
      tags: [Auth]
      summary: Confirm password reset with token
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PasswordResetConfirm'
      responses:
        '200':
          description: Password changed successfully
        '400':
          description: Invalid or expired token
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /auth/oauth/{provider}:
    post:
      tags: [Auth]
      summary: Authenticate via OAuth provider (Google, GitHub, VK)
      security: []
      parameters:
        - in: path
          name: provider
          required: true
          schema:
            type: string
            enum: [google, github, vk]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [code]
              properties:
                code:
                  type: string
                  description: OAuth authorization code from provider
                  example: 4/0AX4XfWi...
      responses:
        '200':
          description: OAuth login/registration successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenResponse'
        '400':
          $ref: '#/components/responses/ValidationError'

  # ══════════ CATALOG ══════════

  /catalog:
    get:
      tags: [Catalog]
      summary: List and search courses in the catalog
      security: []
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/PerPageParam'
        - in: query
          name: q
          schema:
            type: string
          description: Search query string
          example: python
        - in: query
          name: category_id
          schema:
            type: integer
          description: Filter by category ID
          example: 4
        - in: query
          name: free
          schema:
            type: boolean
          description: Filter for free courses only
          example: true
        - in: query
          name: cert
          schema:
            type: boolean
          description: Filter courses that offer certificates
          example: true
        - in: query
          name: language
          schema:
            type: string
          description: Filter by course language (e.g. "ru", "en")
          example: ru
        - in: query
          name: sort
          schema:
            type: string
            enum: [popular, rating, newest]
            default: popular
          description: Sort order
      responses:
        '200':
          description: Paginated list of courses
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/CourseShort'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'

  /catalog/categories:
    get:
      tags: [Catalog]
      summary: List all course categories
      security: []
      responses:
        '200':
          description: List of categories
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Category'

  /catalog/categories/{category_id}:
    get:
      tags: [Catalog]
      summary: Get courses in a specific category
      security: []
      parameters:
        - in: path
          name: category_id
          required: true
          schema:
            type: integer
          example: 400
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/PerPageParam'
      responses:
        '200':
          description: Paginated course list for this category
          content:
            application/json:
              schema:
                type: object
                properties:
                  category:
                    $ref: '#/components/schemas/Category'
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/CourseShort'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'
        '404':
          $ref: '#/components/responses/NotFound'

  # ══════════ COURSES ══════════

  /courses/{course_id}:
    get:
      tags: [Courses]
      summary: Get course detail (promo page)
      security: []
      parameters:
        - in: path
          name: course_id
          required: true
          schema:
            type: integer
          example: 232766
      responses:
        '200':
          description: Course details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CourseDetail'
        '404':
          $ref: '#/components/responses/NotFound'

  /courses/{course_id}/enroll:
    post:
      tags: [Courses]
      summary: Enroll the authenticated user in a course
      parameters:
        - in: path
          name: course_id
          required: true
          schema:
            type: integer
      responses:
        '201':
          description: Enrolled successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Enrollment'
        '400':
          description: Already enrolled
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'

  /courses/{course_id}/unenroll:
    delete:
      tags: [Courses]
      summary: Unenroll the authenticated user from a course
      parameters:
        - in: path
          name: course_id
          required: true
          schema:
            type: integer
      responses:
        '204':
          description: Unenrolled successfully
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'

  # ══════════ MY COURSES (LEARN) ══════════

  /learn/courses:
    get:
      tags: [Courses]
      summary: List courses the authenticated user is enrolled in
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/PerPageParam'
        - in: query
          name: status
          schema:
            type: string
            enum: [in_progress, completed]
          description: Filter by completion status
      responses:
        '200':
          description: Enrolled courses with progress
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      allOf:
                        - $ref: '#/components/schemas/CourseShort'
                        - type: object
                          properties:
                            enrollment:
                              $ref: '#/components/schemas/Enrollment'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'
        '401':
          $ref: '#/components/responses/Unauthorized'

  # ══════════ LESSONS ══════════

  /lessons/{lesson_id}:
    get:
      tags: [Lessons]
      summary: Get a lesson with all its steps
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
          example: 2238910
      responses:
        '200':
          description: Lesson detail with steps
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LessonDetail'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'

  /lessons/{lesson_id}/steps/{step_position}:
    get:
      tags: [Lessons]
      summary: Get a specific step within a lesson
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
          example: 2238910
        - in: path
          name: step_position
          required: true
          schema:
            type: integer
          example: 1
      responses:
        '200':
          description: Step content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Step'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'

  /lessons/{lesson_id}/steps/{step_position}/submit:
    post:
      tags: [Lessons]
      summary: Submit an answer for a step
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
        - in: path
          name: step_position
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StepSubmission'
      responses:
        '200':
          description: Submission result (immediate for quiz/text; pending for code)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmissionResult'
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'

  /submissions/{submission_id}:
    get:
      tags: [Lessons]
      summary: Poll for async submission result (code steps)
      parameters:
        - in: path
          name: submission_id
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Current submission status
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmissionResult'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'

  # ══════════ USERS ══════════

  /users/{user_id}:
    get:
      tags: [Users]
      summary: Get a public user profile
      security: []
      parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
          example: 483341705
      responses:
        '200':
          description: Public user profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
        '404':
          $ref: '#/components/responses/NotFound'

  /users/{user_id}/certificates:
    get:
      tags: [Users]
      summary: Get a user's earned certificates
      security: []
      parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
          example: 637368430
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/PerPageParam'
      responses:
        '200':
          description: List of certificates
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Certificate'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'
        '404':
          $ref: '#/components/responses/NotFound'

  # ══════════ PROFILE (ME) ══════════

  /profile:
    get:
      tags: [Profile]
      summary: Get the authenticated user's own profile
      responses:
        '200':
          description: Current user profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
        '401':
          $ref: '#/components/responses/Unauthorized'

    patch:
      tags: [Profile]
      summary: Update profile info (name, bio, avatar)
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProfileUpdateRequest'
      responses:
        '200':
          description: Updated profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /profile/email:
    put:
      tags: [Profile]
      summary: Change account email address
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EmailUpdateRequest'
      responses:
        '200':
          description: Email updated (verification may be required)
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: A verification link has been sent to your new email.
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /profile/notifications:
    get:
      tags: [Profile]
      summary: Get notification preferences
      responses:
        '200':
          description: Notification preferences
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotificationPreferences'
        '401':
          $ref: '#/components/responses/Unauthorized'

    put:
      tags: [Profile]
      summary: Update notification preferences
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NotificationPreferences'
      responses:
        '200':
          description: Preferences updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotificationPreferences'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /profile/oauth:
    get:
      tags: [Profile]
      summary: List OAuth connections for the current user
      responses:
        '200':
          description: OAuth connections
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/OAuthConnection'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /profile/oauth/{provider}:
    delete:
      tags: [Profile]
      summary: Disconnect an OAuth provider
      parameters:
        - in: path
          name: provider
          required: true
          schema:
            type: string
            enum: [google, github, vk]
      responses:
        '204':
          description: Provider disconnected
        '400':
          description: Cannot disconnect last login method
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          $ref: '#/components/responses/Unauthorized'

  # ══════════ NOTIFICATIONS ══════════

  /notifications:
    get:
      tags: [Notifications]
      summary: Get notifications for the current user
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/PerPageParam'
        - in: query
          name: unread_only
          schema:
            type: boolean
          example: false
      responses:
        '200':
          description: List of notifications
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Notification'
                  unread_count:
                    type: integer
                    example: 3
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /notifications/{notification_id}/read:
    post:
      tags: [Notifications]
      summary: Mark a single notification as read
      parameters:
        - in: path
          name: notification_id
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Notification marked as read
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'

  /notifications/read-all:
    post:
      tags: [Notifications]
      summary: Mark all notifications as read
      responses:
        '204':
          description: All notifications marked as read
        '401':
          $ref: '#/components/responses/Unauthorized'

  # ══════════ TEACHING ══════════

  /teach/courses:
    get:
      tags: [Teaching]
      summary: List courses authored by the current user
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/PerPageParam'
      responses:
        '200':
          description: Instructor's courses
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/CourseShort'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'
        '401':
          $ref: '#/components/responses/Unauthorized'

    post:
      tags: [Teaching]
      summary: Create a new course
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CourseCreateRequest'
      responses:
        '201':
          description: Course created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CourseDetail'
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /teach/courses/{course_id}:
    get:
      tags: [Teaching]
      summary: Get full editable course data (instructor view)
      parameters:
        - in: path
          name: course_id
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Full course data for editing
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CourseDetail'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'

    patch:
      tags: [Teaching]
      summary: Update course metadata
      parameters:
        - in: path
          name: course_id
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CourseUpdateRequest'
      responses:
        '200':
          description: Course updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CourseDetail'
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'

    delete:
      tags: [Teaching]
      summary: Delete a course
      parameters:
        - in: path
          name: course_id
          required: true
          schema:
            type: integer
      responses:
        '204':
          description: Course deleted
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'

  /teach/courses/{course_id}/lessons:
    post:
      tags: [Teaching]
      summary: Add a new lesson to a course module
      parameters:
        - in: path
          name: course_id
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LessonCreateRequest'
      responses:
        '201':
          description: Lesson created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LessonShort'
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'

  /teach/lessons/{lesson_id}:
    patch:
      tags: [Teaching]
      summary: Update a lesson's metadata
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                  example: Updated Lesson Title
                position:
                  type: integer
                  example: 3
      responses:
        '200':
          description: Lesson updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LessonShort'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'

    delete:
      tags: [Teaching]
      summary: Delete a lesson
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
      responses:
        '204':
          description: Lesson deleted
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'

  /teach/lessons/{lesson_id}/steps:
    post:
      tags: [Teaching]
      summary: Add a step to a lesson
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StepCreateRequest'
      responses:
        '201':
          description: Step created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Step'
        '400':
          $ref: '#/components/responses/ValidationError'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'

  /teach/lessons/{lesson_id}/steps/{step_position}:
    patch:
      tags: [Teaching]
      summary: Edit step content
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
        - in: path
          name: step_position
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StepCreateRequest'
      responses:
        '200':
          description: Step updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Step'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'

    delete:
      tags: [Teaching]
      summary: Delete a step
      parameters:
        - in: path
          name: lesson_id
          required: true
          schema:
            type: integer
        - in: path
          name: step_position
          required: true
          schema:
            type: integer
      responses:
        '204':
          description: Step deleted
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
```


```
project/
├── config/                          # Project settings (replaces default "project" folder)
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── apps/
│   ├── users/                       # Auth, profiles, OAuth, notifications
│   │   ├── models.py                # User (extended), OAuthConnection
│   │   ├── serializers.py
│   │   ├── views.py                 # register, login, profile CRUD, oauth
│   │   ├── urls.py
│   │   ├── permissions.py
│   │   └── tasks.py                 # send password reset email (Celery)
│   │
│   ├── courses/                     # Catalog, courses, enrollment
│   │   ├── models.py                # Course, Category, Module, Enrollment
│   │   ├── serializers.py
│   │   ├── views.py                 # catalog, course detail, enroll/unenroll
│   │   ├── urls.py
│   │   └── filters.py               # DRF filtering for catalog search
│   │
│   ├── lessons/                     # Lessons, steps, content
│   │   ├── models.py                # Lesson, Step, StepContent
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── submissions/                 # Answer checking, results
│   │   ├── models.py                # Submission, SubmissionResult
│   │   ├── serializers.py
│   │   ├── views.py                 # submit answer, poll result
│   │   ├── urls.py
│   │   ├── tasks.py                 # ← Celery: run code, check answer async
│   │   └── checkers/
│   │       ├── base.py              # Abstract checker interface
│   │       ├── quiz.py              # Instant answer check
│   │       └── code.py              # Sandboxed code runner
│   │
│   ├── notifications/               # User notifications
│   │   ├── models.py                # Notification
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tasks.py                 # Celery: dispatch notifications
│   │
│   └── analytics/                   # Progress, statistics
│       ├── models.py                # UserCourseProgress, StepCompletion
│       ├── serializers.py
│       ├── views.py                 # progress %, leaderboard, stats
│       ├── urls.py
│       └── tasks.py                 # Celery: aggregate stats, update Redis cache
│
├── templates/                       # HTMX/Django templates
│   ├── base.html
│   ├── partials/                    # HTMX partial responses
│   │   ├── course_card.html
│   │   ├── step_content.html
│   │   └── notification_list.html
│   ├── courses/
│   ├── lessons/
│   └── users/
│
├── static/
│   ├── css/
│   ├── js/
│   └── htmx/
│
├── docker-compose.yml               # Django + PostgreSQL + Redis + RabbitMQ + Celery
├── Dockerfile
├── requirements.txt
└── manage.py
```
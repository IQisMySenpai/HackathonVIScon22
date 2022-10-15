# API Endpoints
## Course Info by ID
### Request
`POST /api/courseByID`

### Parameters
- `course_id` - The ID of the course to get information about

### Response
- `course_id` - The ID of the course
- `course_name` - The name of the course
- `course_description` - The description of the course
- `course_instructor` - The name of the instructor (if picture is available, else `null`)
- `course_instructor_picture` - The picture of the instructor (if available, else `null`)
- `course_tags` - The tags associated with the course
   - `name` - The name of the tag
   - `color` - The color of the tag
- `course_rating` - The rating of the course
   - `name` - The name of the rating
   - `value` - The value of the rating

## Add Review
### Request
`POST /api/addReview`

### Parameters
- `course_id` - The ID of the course to add a review to
- `user_id` - The ID of the user adding the review
- `review_text` - The text of the review
- `review_ratings` - Array of ratings of the course
    - `name` - The name of the rating
    - `value` - The value of the rating
- `review_tags` - Array of tags of the course
    - `name` - The name of the tag
    - `color` - The color of the tag
- `pros` - Array of pros of the course
- `cons` - Array of cons of the course

### Response
- `success` - Whether the review was successfully added
- `id` - The ID of the review

## Get Reviews
### Request
`POST /api/getReviews`

### Parameters
- `course_id` - The ID of the course to get reviews for
- `number` - The number of reviews to get
- `offset` - The offset of the reviews to get
- `sort` - The sort of the reviews to get
   - `newest` - Newest reviews first
   - `oldest` - Oldest reviews first
   - `highest` - Highest rated reviews first
   - `lowest` - Lowest rated reviews first

### Response
- `reviews` - Array of reviews
   - `id` - The ID of the review
   - `user_id` - The ID of the user who wrote the review
   - `user_name` - The name of the user who wrote the review
   - `review_text` - The text of the review
   - `review_ratings` - Array of ratings of the course
      - `name` - The name of the rating
      - `value` - The value of the rating
   - `review_tags` - Array of tags of the course
      - `name` - The name of the tag
      - `color` - The color of the tag
   - `pros` - Array of pros of the course
   - `cons` - Array of cons of the course
   - `date` - The date the review was written

## Report Review
### Request
`POST /api/reportReview`

### Parameters
- `review_id` - The ID of the review to report

### Response
- `success` - Whether the review was successfully reported
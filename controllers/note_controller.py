import json
from base_controller import Handlers, authenticate_user
from models import User, Note

class NoteAdd(Handlers):
	@authenticate_user
	def post(self):
		access_token = self.request.get("access_token")
		title = self.request.get("title")
		content = self.request.get("content")

		self.response.headers['Content-Type'] = 'application/json'
		note = Note.add(user=self.user, title=title, content=content)
		if note:
			response = {
				"status": "success",
				"message": "Successfully add new note",
			}
			self.response.out.write(json.dumps(response))
		else:
			response = {
				"status": "fail",
				"message": "Failed to add note",
			}
			self.response.out.write(json.dumps(response))

class NoteGetAll(Handlers):
	@authenticate_user
	def get(self):
		notes = Note.get_all_by_specific_user(user=self.user)
		self.response.headers['Content-Type'] = 'application/json'

		list_of_json_notes = []
		for note in notes:
			list_of_json_notes.append({
				"title": note.title,
				"content": note.content,
				"createdDate": note.created_date.isoformat(),
			})
		response = {
			"notes": list_of_json_notes,
		}
		self.response.out.write(json.dumps(response))

class NoteGetSome(Handlers):
	@authenticate_user
	def get(self, user_key):
		self.response.headers['Content-Type'] = 'application/json'
		if status:
			response = {
				"status": "success",
				"data": "Logout Successfully",
			}
			self.response.out.write(json.dumps(response))
		else:
			response = {
				"status": "fail",
				"message": "",
			}
			self.response.set_status(403, message="Forbidden")
			self.response.out.write(json.dumps(response))

class NoteUpdate(Handlers):
	@authenticate_user
	def post(self, user_key):
		note_id = self.request.get("note-id")
		title = self.request.get("title")
		content = self.request.get("content")
		note_id = self.request.get("note-id")
		note_id = Note.update(note_id)
		if note_id:
			response = {
				"status": "success",
				"message": "Delete note successfully",
			}
			self.response.out.write(json.dumps(response))
		else:
			response = {
				"status": "fail",
				"message": "Failed to delete note",
			}
			self.response.set_status(403, message="Forbidden")
			self.response.out.write(json.dumps(response))

class NoteDelete(Handlers):
	@authenticate_user
	def post(self, user_key):
		note_id = self.request.get("note-id")
		note_id = Note.delete(note_id)
		if note_id:
			response = {
				"status": "success",
				"message": "Delete note successfully",
			}
			self.response.out.write(json.dumps(response))
		else:
			response = {
				"status": "fail",
				"message": "Failed to delete note",
			}
			self.response.set_status(403, message="Forbidden")
			self.response.out.write(json.dumps(response))

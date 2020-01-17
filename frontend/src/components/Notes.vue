<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Note Keeping System</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.note-modal>Add Note</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Note</th>
              <th scope="col">User</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(note, id) in notes" :key="id">
              <td>{{ note.Note }}</td>
              <td>{{ note.User }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.note-update-modal
                          @click="editNote(note)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteNote(note)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addNoteModal"
            id="note-modal"
            note="Add a new note"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-note-group"
                    label="Note:"
                    label-for="form-note-input">
          <b-form-input id="form-note-input"
                        type="text"
                        v-model="addNoteForm.note"
                        required
                        placeholder="Enter note">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-user-group"
                      label="User:"
                      label-for="form-user-input">
            <b-form-input id="form-user-input"
                          type="text"
                          v-model="addNoteForm.user"
                          required
                          placeholder="Enter user">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editNoteModal"
            id="note-update-modal"
            note="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-note-edit-group"
                    label="Note:"
                    label-for="form-note-edit-input">
          <b-form-input id="form-note-edit-input"
                        type="text"
                        v-model="editForm.note"
                        required
                        placeholder="Enter note">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-user-edit-group"
                      label="User:"
                      label-for="form-user-edit-input">
            <b-form-input id="form-user-edit-input"
                          type="text"
                          v-model="editForm.user"
                          required
                          placeholder="Enter user">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      notes: [],
      addNoteForm: {
        note: '',
        user: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        note: '',
        user: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getNotes() {
      const path = 'http://localhost:5000/api/v1/resources/notes/';
      axios.get(path)
        .then((res) => {
          this.notes = res.data.notes;
          console.log(res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addNote(payload) {
      console.log(payload);
      const path = 'http://localhost:5000/api/v1/resources/notes/';
      axios.post(path, payload)
        .then(() => {
          this.getNotes();
          this.message = 'The Note has been added to the list!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getNotes();
        });
    },
    initForm() {
      this.addNoteForm.note = '';
      this.addNoteForm.user = '';
      this.editForm.id = '';
      this.editForm.note = '';
      this.editForm.user = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addNoteModal.hide();
      const payload = {
        note: this.addNoteForm.note,
        user: this.addNoteForm.user,
      };
      this.addNote(payload);
      console.log(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addNoteModal.hide();
      this.initForm();
    },
    editNote(note) {
      this.editForm = note;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editNoteModal.hide();
      const payload = {
        note: this.editForm.note,
        user: this.editForm.user,
      };
      this.updateNote(payload, this.editForm.id);
    },
    updateNote(payload, noteID) {
      const path = `http://localhost:5000/api/v1/resources/notes/${noteID}`;
      axios.put(path, payload)
        .then(() => {
          this.getNotes();
          this.message = 'Note updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getNotes();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editNoteModal.hide();
      this.initForm();
      this.getNotes();
    },
    removeNote(noteID) {
      const path = `http://localhost:5000/api/v1/resources/notes/${noteID}`;
      axios.delete(path)
        .then(() => {
          this.getNotes();
          this.message = 'Note removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getNotes();
        });
    },
    onDeleteNote(note) {
      this.removeNote(note.id);
    },
  },
  created() {
    this.getNotes();
  },
};
</script>

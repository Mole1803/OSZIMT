class Question_card extends HTMLElement {


    add_answer(question_id) {
        let answer_choices = this.querySelector(".answer-choices");
        let answer_index = answer_choices.childElementCount + 1;

        answer_choices.innerHTML += `
        <div class="form-group">
            <label for="answer_${this.question_id}_${answer_index}">Answer ${answer_index}</label>
            <input type="text" name="answer_${this.question_id}_${answer_index}" id="answer_${this.question_id}_${answer_index}" class="form-control answer">
        </div>
        `;
    }

    remove_answer() {
        let answer_choices = this.querySelector(".answer-choices");
        //check if there is more than one answer
        if (answer_choices.childElementCount > 1) {
            //TODO bug there is an empty string stored as the last child
            answer_choices.removeChild(answer_choices.lastChild);
            answer_choices.removeChild(answer_choices.lastChild);
        }
    }


    constructor() {
        super();
    }

    connectedCallback() {
        if (!this.id)
            this.id = "_id"
        console.log(this.id)
        this.question_id = this.attributes.question_id.value;
        this.innerHTML = `
        <div class="card" style="margin-top: 2%; margin-bottom: 2%">
            <div class="card-header">
                <h3>Question 1</h3>
            </div>
            <div class="card-body" >
                <div class="form-group">
                    <label for="question_${this.question_id}">Question</label>
                    <input type="text" name="question_${this.question_id}" id="question_${this.question_id}" class="form-control question">
                </div>
                <div class="answer-choices">
                    <div class="form-group">
                        <label for="answer_${this.question_id}_1">Answer 1</label>
                        <input type="text" name="answer_${this.question_id}_1" id="answer_${this.question_id}_1" class="form-control answer">
                    </div>
                </div>
                <div class="container text-center">
                    <button type="button" class="btn btn-primary" id="add-answer-${this.id}" onclick="${this.id}.add_answer(${this.question_id})">Add Answer</button>
                    <button type="button" class="btn btn-primary" id="remove-answer-${this.id}" onclick="${this.id}.remove_answer()">Remove Answer</button>
                </div>
            </div>
        </div>
        `;
    }


}

customElements.define('question-card', Question_card);


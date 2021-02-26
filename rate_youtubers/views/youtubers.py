from flask import Blueprint, render_template, g, redirect, url_for

from ..models import Youtuber
from ..extensions import db
from ..forms import YoutuberForm

youtubers = Blueprint('youtubers', __name__)


@youtubers.route('/', methods=['POST', 'GET'])
def create():
    form = YoutuberForm()

    if form.validate_on_submit():
        print(form)
        id = form.id.data
        name = form.name.data
        description = form.description.data
        if Youtuber.query.get(id) is not None:
            return 'YouTuber already registered.', 400
        youtuber = Youtuber(id=id, name=name, description=description)
        db.session.add(youtuber)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('pages/youtubers.html', form=form)

import os
from flask import Blueprint, render_template, g, redirect, url_for

from ..models import Youtuber
from ..extensions import db, youtube
from ..forms import YoutuberForm

youtubers = Blueprint('youtubers', __name__)


@youtubers.route('/', methods=['POST', 'GET'])
def create():
    form = YoutuberForm()

    if form.validate_on_submit():
        print('ok')
        link = form.link.data
        link_type, id = link.split('/')[-2:]
        if link_type == 'channel':
            options = {'id': id}
        elif link_type == 'user':
            options = {'forUsername': id}
        request = youtube.channels().list(
            part='snippet',
            # forUsername=link
            **options
        )
        response = request.execute()
        if response['pageInfo']['totalResults'] == 0:
            return 404

        # this is messy asf
        channel_info = response['items'][0]['snippet']
        avatar = channel_info['thumbnails']['default']['url']
        name = channel_info['title']
        description = channel_info['description']
        id = response['items'][0]['id']

        relevant_info = {
            'channel_info': channel_info,
            'avatar': avatar,
            'name': name,
            'id': id,
            'description': description,
        }

        return render_template('pages/rate-youtuber.html', **relevant_info)

    return render_template('pages/find-youtuber.html', form=form)

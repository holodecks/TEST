from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# 相談フォームの定義
class ConsultationForm(FlaskForm):
    name = StringField('お名前', validators=[DataRequired(message='お名前を入力してください')])
    email = StringField('メールアドレス', validators=[DataRequired(message='メールアドレスを入力してください'), Email(message='有効なメールアドレスを入力してください')])
    age = StringField('年齢')
    category = SelectField('相談カテゴリー', choices=[
        ('pregnancy', '妊娠・出産'),
        ('postpartum', '産後ケア'),
        ('breastfeeding', '授乳'),
        ('womens_health', '女性の健康'),
        ('other', 'その他')
    ])
    message = TextAreaField('相談内容', validators=[DataRequired(message='相談内容を入力してください')])

# 相談データを保存するリスト（本番環境ではデータベースを使用）
consultations = []

@app.route('/')
def index():
    """トップページ"""
    return render_template('index.html')

@app.route('/about')
def about():
    """助産師紹介ページ"""
    return render_template('about.html')

@app.route('/consultation', methods=['GET', 'POST'])
def consultation():
    """相談フォームページ"""
    form = ConsultationForm()
    if form.validate_on_submit():
        # フォームデータを保存
        consultation_data = {
            'id': len(consultations) + 1,
            'name': form.name.data,
            'email': form.email.data,
            'age': form.age.data,
            'category': form.category.data,
            'message': form.message.data,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        consultations.append(consultation_data)
        flash('ご相談を受け付けました。担当の助産師から24時間以内にご連絡いたします。', 'success')
        return redirect(url_for('consultation'))
    return render_template('consultation.html', form=form)

@app.route('/health-info')
def health_info():
    """健康情報ページ"""
    # 健康情報のサンプルデータ
    articles = [
        {
            'title': '妊娠初期の過ごし方',
            'summary': '妊娠初期は体調の変化が大きい時期です。つわりや眠気などの症状への対処法をご紹介します。',
            'category': 'pregnancy'
        },
        {
            'title': '産後の骨盤ケア',
            'summary': '出産後の骨盤は緩んだ状態です。適切なケアで体型の回復をサポートしましょう。',
            'category': 'postpartum'
        },
        {
            'title': '母乳育児のコツ',
            'summary': '母乳育児を成功させるための授乳姿勢や頻度、トラブル対処法について解説します。',
            'category': 'breastfeeding'
        },
        {
            'title': '女性のライフステージと健康',
            'summary': '思春期から更年期まで、女性の体は様々な変化を経験します。各ステージでのケアのポイントをお伝えします。',
            'category': 'womens_health'
        }
    ]
    return render_template('health_info.html', articles=articles)

@app.route('/contact')
def contact():
    """お問い合わせページ"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

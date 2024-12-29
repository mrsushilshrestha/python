
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Grid Gallery</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
            .gallery-container { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; width: 90%; max-width: 1200px; background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
            .gallery-item { position: relative; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); transition: transform 0.3s ease; }
            .gallery-item img { width: 100%; height: auto; border-radius: 10px; object-fit: cover; }
            .gallery-item:hover { transform: scale(1.05); }
            .image-caption { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: rgba(0, 0, 0, 0.6); color: white; padding: 10px 20px; font-size: 18px; border-radius: 5px; opacity: 0; transition: opacity 0.3s ease; }
            .gallery-item:hover .image-caption { opacity: 1; }
            @media (max-width: 1200px) { .gallery-container { grid-template-columns: repeat(3, 1fr); } }
            @media (max-width: 768px) { .gallery-container { grid-template-columns: repeat(2, 1fr); } }
            @media (max-width: 480px) { .gallery-container { grid-template-columns: 1fr; } }
        </style>
    </head>
    <body>

    <div class="gallery-container">
    
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-1-1.png" alt="Snapshot 1">
            <div class="image-caption">Snapshot 1</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-1-2.png" alt="Snapshot 2">
            <div class="image-caption">Snapshot 2</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-1.png" alt="Snapshot 3">
            <div class="image-caption">Snapshot 3</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-10-1-Tupple-Method.png" alt="Snapshot 4">
            <div class="image-caption">Snapshot 4</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-10-Tupple.png" alt="Snapshot 5">
            <div class="image-caption">Snapshot 5</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-2-1.png" alt="Snapshot 6">
            <div class="image-caption">Snapshot 6</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-2-2.png" alt="Snapshot 7">
            <div class="image-caption">Snapshot 7</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-2.png" alt="Snapshot 8">
            <div class="image-caption">Snapshot 8</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-3.png" alt="Snapshot 9">
            <div class="image-caption">Snapshot 9</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-4-1.png" alt="Snapshot 10">
            <div class="image-caption">Snapshot 10</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-4.png" alt="Snapshot 11">
            <div class="image-caption">Snapshot 11</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-5.png" alt="Snapshot 12">
            <div class="image-caption">Snapshot 12</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-6.png" alt="Snapshot 13">
            <div class="image-caption">Snapshot 13</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-7-1.png" alt="Snapshot 14">
            <div class="image-caption">Snapshot 14</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-7.png" alt="Snapshot 15">
            <div class="image-caption">Snapshot 15</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-8-1.png" alt="Snapshot 16">
            <div class="image-caption">Snapshot 16</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-8-2.png" alt="Snapshot 17">
            <div class="image-caption">Snapshot 17</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-8-3.png" alt="Snapshot 18">
            <div class="image-caption">Snapshot 18</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-8-output.png" alt="Snapshot 19">
            <div class="image-caption">Snapshot 19</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-8.png" alt="Snapshot 20">
            <div class="image-caption">Snapshot 20</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9-1.png" alt="Snapshot 21">
            <div class="image-caption">Snapshot 21</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9-2.png" alt="Snapshot 22">
            <div class="image-caption">Snapshot 22</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9-3.png" alt="Snapshot 23">
            <div class="image-caption">Snapshot 23</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9-4.png" alt="Snapshot 24">
            <div class="image-caption">Snapshot 24</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9-5.png" alt="Snapshot 25">
            <div class="image-caption">Snapshot 25</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9-6.png" alt="Snapshot 26">
            <div class="image-caption">Snapshot 26</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9-7.png" alt="Snapshot 27">
            <div class="image-caption">Snapshot 27</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-9.png" alt="Snapshot 28">
            <div class="image-caption">Snapshot 28</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-11.png" alt="Snapshot 29">
            <div class="image-caption">Snapshot 29</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-11-1-dic-method.png" alt="Snapshot 30">
            <div class="image-caption">Snapshot 30</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-11-0.png" alt="Snapshot 31">
            <div class="image-caption">Snapshot 31</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/tuple.png" alt="Snapshot 32">
            <div class="image-caption">Snapshot 32</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-11-dic.png" alt="Snapshot 33">
            <div class="image-caption">Snapshot 33</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-CRUD.png" alt="Snapshot 34">
            <div class="image-caption">Snapshot 34</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-CRUD-image.png" alt="Snapshot 35">
            <div class="image-caption">Snapshot 35</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-CRUD-image2.png" alt="Snapshot 36">
            <div class="image-caption">Snapshot 36</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-1-CRUD.png" alt="Snapshot 37">
            <div class="image-caption">Snapshot 37</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-2-CRUD.png" alt="Snapshot 38">
            <div class="image-caption">Snapshot 38</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-3-CRUD.png" alt="Snapshot 39">
            <div class="image-caption">Snapshot 39</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-4-CRUD.png" alt="Snapshot 40">
            <div class="image-caption">Snapshot 40</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-5-CRUD.png" alt="Snapshot 41">
            <div class="image-caption">Snapshot 41</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-6-CRUD.png" alt="Snapshot 42">
            <div class="image-caption">Snapshot 42</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-7-CRUD.png" alt="Snapshot 43">
            <div class="image-caption">Snapshot 43</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/CRUD-background.png" alt="Snapshot 44">
            <div class="image-caption">Snapshot 44</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-12-CRUD-Backgroud.png" alt="Snapshot 45">
            <div class="image-caption">Snapshot 45</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/DSA-in-python.png" alt="Snapshot 46">
            <div class="image-caption">Snapshot 46</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/DSA-in-python-background.png" alt="Snapshot 47">
            <div class="image-caption">Snapshot 47</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-13-SET.png" alt="Snapshot 48">
            <div class="image-caption">Snapshot 48</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-14-function.png" alt="Snapshot 49">
            <div class="image-caption">Snapshot 49</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-14-1-function.png" alt="Snapshot 50">
            <div class="image-caption">Snapshot 50</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-14-2-function.png" alt="Snapshot 51">
            <div class="image-caption">Snapshot 51</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-14-3-function.png" alt="Snapshot 52">
            <div class="image-caption">Snapshot 52</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-14-4-function.png" alt="Snapshot 53">
            <div class="image-caption">Snapshot 53</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-14-5-function.png" alt="Snapshot 54">
            <div class="image-caption">Snapshot 54</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-14-6-function.png" alt="Snapshot 55">
            <div class="image-caption">Snapshot 55</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-15-recursion.png" alt="Snapshot 56">
            <div class="image-caption">Snapshot 56</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/day-15-recursion-.png" alt="Snapshot 57">
            <div class="image-caption">Snapshot 57</div>
        </div>
        
        <div class="gallery-item">
            <img src="https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/lamda.png" alt="Snapshot 58">
            <div class="image-caption">Snapshot 58</div>
        </div>
        
    </div>

    </body>
    </html>
    
(function(){ // scoping

    // Adding the #link
    $("main > h1").each(function(i, el) {
	var el = $(el);
	var id = el.attr('id');
	//var link = '<i class="fa fa-link"></i>';
	var link = '¶';
	if (id) {
	    return el.append($("<a />").addClass("header-link").attr("href", "#" + id).html(link));
	}
    });


    var hash = window.location.hash.slice(1)

    var collapsable = []

    $('main h1.collapse-trigger').each(function() {
    	var handle = $(this);
	handle.nextUntil('h1').wrapAll('<section></section>'); // early
    	collapsable.push(handle);
    	var id = handle.attr('id');
    	if( (id != undefined && id == hash) ){ handle.addClass('open'); }
    	handle.on('click',function(){ handle.toggleClass('open'); return false; }); // Don't propagate (to header-links). People can right-click
    });


    if(collapsable.length > 1){
    	$('<span class="collapse-menu">[Expand all]</span>').prependTo('main').on('click',function(){
    	    for (var i = 0; i < collapsable.length; i++) { collapsable[i].addClass('open'); }
    	});
    	$('<span class="collapse-menu">[Collapse all]</span>').prependTo('main').on('click',function(){
    	    for (var i = 0; i < collapsable.length; i++) { collapsable[i].removeClass('open'); }
    	});
	
    }

    // Make indentation visible
    $('main .language-python pre.codehilite code').each(function() {
	var o = $(this);
	var t = o.html();
	var n = t.replace(/\t/g, "<span class='indent'>\t</span>")
	o.html(n);
    });

})()
